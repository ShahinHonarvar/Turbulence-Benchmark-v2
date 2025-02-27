from itertools import combinations

def lists_with_product_equal_n(circular_list):
    prod = 4
    sublists = []
    for i in range(len(circular_list)):
        for j in range(i + 1, len(circular_list)):
            product = 1
            for k in range(i, j + 1):
                product *= circular_list[k]
            if product == prod:
                sublists.append(circular_list[i:j + 1])
    return sublists