from itertools import islice, cycle

def lists_with_product_equal_n(lst):

    def sublists_with_product_equal_n(lst, n):
        result = []
        for i in range(1, len(lst) + 1):
            for j in range(len(lst) - i + 1):
                sublist = lst[j:j + i]
                if j > 0 and lst[j - 1] == lst[j]:
                    continue
                if j + i < len(lst) and lst[j + i] == lst[j]:
                    continue
                if prod(sublist) == n:
                    result.append(sublist)
        return result

    def prod(lst):
        p = 1
        for i in lst:
            p *= i
        return p
    return sublists_with_product_equal_n(list(cycle(lst)), 33)