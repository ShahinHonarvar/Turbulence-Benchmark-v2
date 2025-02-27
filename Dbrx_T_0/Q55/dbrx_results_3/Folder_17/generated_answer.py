from itertools import islice, cycle

def lists_with_product_equal_n(lst):

    def sublists_with_product_equal_n(lst, n):
        result = []
        for i in range(1, len(lst) + 1):
            for j in range(len(lst) - i + 1):
                if prod(lst[j:j + i]) == n:
                    result.append(lst[j:j + i])
        return result

    def prod(lst):
        return reduce(lambda x, y: x * y, lst, 1)
    return sublists_with_product_equal_n(lst, 18) + sublists_with_product_equal_n(list(islice(cycle(lst), len(lst) - 1, None)), 18)