from itertools import combinations

def lists_with_product_equal_n(circular_list):
    sublists = []
    for i in range(1, len(circular_list) + 1):
        sublists.extend(list(combinations(circular_list, i)))
    result = []
    for sublist in sublists:
        if len(sublist) < len(circular_list) and reduce(lambda x, y: x * y, sublist) == -30:
            result.append(list(sublist))
    return result