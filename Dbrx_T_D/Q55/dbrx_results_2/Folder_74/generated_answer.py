from itertools import islice

def lists_with_product_equal_n(lst):

    def sublists_with_product_equal_n(lst, n):
        for i in range(len(lst)):
            for j in range(i, len(lst)):
                if j > i and lst[j] == 1:
                    continue
                if prod(lst[i:j + 1]) == n:
                    yield lst[i:j + 1]
                if prod(lst[i:j + 1]) > n:
                    break

    def prod(lst):
        p = 1
        for i in lst:
            p *= i
        return p

    def circular_shifts(lst):
        for i in range(len(lst)):
            yield (lst[i:] + lst[:i])
    return [sl for sl in {sl for sl in [sublists_with_product_equal_n(sublst, 51) for sublst in circular_shifts(lst)] if sl} if sl]