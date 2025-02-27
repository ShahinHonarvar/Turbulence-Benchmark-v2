from itertools import combinations

def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    extended_list = circular_list + circular_list[:-1]
    for size in range(1, n + 1):
        for start in range(n):
            sublist = extended_list[start:start + size]
            product = 1
            for num in sublist:
                product *= num
                if product == 0:
                    break
            if product == 45:
                result.append(sublist)
    return result