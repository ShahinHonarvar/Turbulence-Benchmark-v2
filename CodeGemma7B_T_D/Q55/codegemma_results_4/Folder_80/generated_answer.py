from itertools import combinations

def lists_with_product_equal_n(circular_list):
    for i in range(len(circular_list)):
        sublists = []
        for j in range(i, len(circular_list)):
            product = 1
            for k in circular_list[j:j + j - i + 1]:
                product *= k
            if product == 43:
                sublists.append(circular_list[j:j + j - i + 1])
    return sublists