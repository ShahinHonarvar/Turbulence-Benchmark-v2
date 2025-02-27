from itertools import combinations

def lists_with_product_equal_n(circular_list):

    def product(lst):
        result = 1
        for i in lst:
            result *= i
        return result
    sublists = []
    for i in range(1, len(circular_list) + 1):
        sublists.extend(combinations(circular_list, i))
    result = []
    for sublist in sublists:
        if product(sublist) == -36:
            result.append(list(sublist))
    return result