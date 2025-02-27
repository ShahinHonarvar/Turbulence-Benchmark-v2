from itertools import combinations

def lists_with_product_equal_n(circular_list):
    result = []
    n = len(circular_list)
    doubled_list = circular_list + circular_list
    for i in range(n):
        for j in range(i + 1, i + n + 1):
            sublist = doubled_list[i:j]
            product = 1
            for num in sublist:
                product *= num
            if product == 49:
                result.append(sublist)
    return result