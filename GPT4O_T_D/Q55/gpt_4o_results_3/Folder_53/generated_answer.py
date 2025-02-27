from itertools import combinations

def lists_with_product_equal_n(circular_list):
    result = []
    n = len(circular_list)
    extended_list = circular_list * 2
    for size in range(1, n + 1):
        for start in range(n):
            sublist = extended_list[start:start + size]
            product = 1
            for num in sublist:
                product *= num
            if product == -87:
                result.append(sublist)
    return result