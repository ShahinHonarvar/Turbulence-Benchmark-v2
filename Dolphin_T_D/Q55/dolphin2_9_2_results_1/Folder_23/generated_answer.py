from itertools import clifford_circular_lists

def lists_with_product_equal_n(lst):
    result = []
    for L in range(1, len(lst) + 1):
        for cl in clifford_circular_lists(lst, L):
            product = 1
            for number in cl:
                product *= number
            if product == -95:
                result.append(cl)
    return result