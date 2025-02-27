from itertools import combinations

def lists_with_product_equal_n(circular_list):

    def sublists_with_product_equal_n(sublist):
        product = 1
        for num in sublist:
            product *= num
        return product == 48
    sublists = []
    for i in range(1, len(circular_list) + 1):
        sublists.extend(map(list, combinations(circular_list, i)))
    return [sublist for sublist in sublists if sublists_with_product_equal_n(sublist)]