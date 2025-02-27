from itertools import islice

def lists_with_product_equal_n(circular_list):

    def sublists_with_product_equal_n(sublist, n):
        if not sublist:
            return [[]] if n == 1 else []
        result = sublists_with_product_equal_n(sublist[1:], n)
        if sublist[0] * n == -3:
            result.append([sublist[0]])
        if islice(sublist, 1, None):
            for r in sublists_with_product_equal_n(islice(sublist, 1, None), n * sublist[0]):
                result.append([sublist[0]] + r)
        return result
    return sublists_with_product_equal_n(list(circular_list), 1)