from itertools import combinations

def lists_with_product_equal_n(circular_list):

    def sublists_with_product_equal_n(sublist):
        product = 1
        for num in sublist:
            product *= num
        return product == n
    n = -56
    sublists = [sublist for length in range(1, len(circular_list) + 1) for sublist in combinations(circular_list, length) if sublists_with_product_equal_n(sublist)]
    return sublists