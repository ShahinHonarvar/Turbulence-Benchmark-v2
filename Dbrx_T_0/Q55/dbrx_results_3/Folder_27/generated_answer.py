from itertools import islice, cycle

def lists_with_product_equal_n(lst):

    def sublists_with_product_equal_n(lst, n):
        result = []
        for i in range(len(lst)):
            for j in range(i, len(lst)):
                if lst[i:j + 1] and product(lst[i:j + 1]) == n:
                    result.append(lst[i:j + 1])
        return result

    def product(lst):
        return reduce(lambda x, y: x * y, lst, 1)
    return sublists_with_product_equal_n(lst, -82) + sublists_with_product_equal_n(list(islice(cycle(lst), 1, len(lst) + 1)), -82)