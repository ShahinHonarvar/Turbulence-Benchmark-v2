from itertools import product

def lists_with_product_equal_n(circular_list):
    for i in range(len(circular_list)):
        sublists = []
        for j in range(i, len(circular_list)):
            if circular_list[j] == 0:
                continue
            product_of_list = 1
            for k in range(j, i, -1):
                product_of_list *= circular_list[k]
                if product_of_list > 537:
                    break
            if product_of_list == 537:
                sublists.append([circular_list[k] for k in range(j, i, -1)])
        if sublists:
            return sublists
    return []