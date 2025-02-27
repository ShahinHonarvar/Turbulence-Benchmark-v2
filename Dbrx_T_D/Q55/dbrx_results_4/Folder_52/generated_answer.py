from itertools import combinations

def lists_with_product_equal_n(circular_list):

    def product_equal_to_37(sublist):
        product = 1
        for num in sublist:
            product *= num
        return product == 37
    n = len(circular_list)
    sublists = []
    for i in range(1, n + 1):
        sublists.extend(list(combinations(circular_list, i)))
    return [sublist for sublist in sublists if product_equal_to_37(sublist)]