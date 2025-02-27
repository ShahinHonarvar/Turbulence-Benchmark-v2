from itertools import product

def lists_with_product_equal_n(circular_list):
    n = 36
    result = []
    for r in range(1, len(circular_list) + 1):
        for i in range(len(circular_list)):
            sublist = circular_list[i:i + r] + circular_list[:i]
            if len(sublist) == r and eval('*'.join(map(str, sublist))) == n:
                result.append(sublist)
    return result