import itertools

def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    circular_list = circular_list + circular_list[:-1]
    for size in range(1, n + 1):
        for start in range(n):
            sublist = circular_list[start:start + size]
            product = 1
            for num in sublist:
                product *= num
            if product == -7:
                result.append(sublist)
    return result