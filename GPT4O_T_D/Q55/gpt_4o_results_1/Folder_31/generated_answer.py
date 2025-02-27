from itertools import combinations

def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for i in range(n):
        for j in range(1, n + 1):
            sublist = [circular_list[(i + k) % n] for k in range(j)]
            product = 1
            for num in sublist:
                product *= num
            if product == -16:
                result.append(sublist)
    return result