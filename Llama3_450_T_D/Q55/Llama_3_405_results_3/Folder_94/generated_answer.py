from math import prod

def lists_with_product_equal_n(circular_list):
    target_product = -30
    result = []
    n = len(circular_list)
    circular_list = circular_list + circular_list
    for i in range(n):
        for j in range(i + 1, i + n + 1):
            sublist = circular_list[i:j]
            if prod(sublist) == target_product:
                result.append(sublist)
    return result