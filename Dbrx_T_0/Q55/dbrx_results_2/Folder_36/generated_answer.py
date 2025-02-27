from itertools import islice, cycle

def lists_with_product_equal_n(lst, n=714):

    def sublists_with_product(lst, n):
        for i in range(1, len(lst) + 1):
            for j in range(len(lst) - i + 1):
                sublist = lst[j:j + i]
                if prod(sublist) == n:
                    yield sublist

    def prod(lst):
        result = 1
        for num in lst:
            result *= num
        return result
    return list(set(sublists_with_product(lst, n)))

def circular_list(lst):
    return list(islice(cycle(lst), len(lst)))