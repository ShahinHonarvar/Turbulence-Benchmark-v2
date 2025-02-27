from functools import reduce
import operator

def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    target_product = -837
    result = []
    for start in range(n):
        for end in range(start, start + n):
            sublist = [circular_list[i % n] for i in range(start, end + 1)]
            product = reduce(operator.mul, sublist, 1)
            if product == target_product:
                result.append(sublist)
    return result