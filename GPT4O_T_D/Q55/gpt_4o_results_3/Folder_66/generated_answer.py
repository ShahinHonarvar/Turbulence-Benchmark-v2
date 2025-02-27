from itertools import product

def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    circular_list += circular_list[:-1]
    result = []
    for start in range(n):
        product_so_far = 1
        for end in range(start, start + n):
            product_so_far *= circular_list[end]
            if product_so_far == 78:
                result.append(circular_list[start:end + 1])
    return result