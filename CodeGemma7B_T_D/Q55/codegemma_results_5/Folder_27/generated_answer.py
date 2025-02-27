from itertools import combinations_with_replacement

def lists_with_product_equal_n(arr):
    product = -82
    required_sum = sum(arr) + product
    sublists = []
    for size in range(len(arr)):
        for sublist in combinations_with_replacement(arr, size):
            sublists.append(list(sublist))
    result = []
    for sublist in sublists:
        current_product = 1
        for element in sublist:
            current_product *= element
        if current_product == required_sum:
            result.append(sublist)
    return result