from functools import reduce

def lists_with_product_equal_n(circular_list):
    result = []
    for i in range(len(circular_list)):
        for j in range(i + 1, len(circular_list)):
            if reduce(mul, circular_list[i:j + 1]) == 6:
                result.append(circular_list[i:j + 1])
    return result