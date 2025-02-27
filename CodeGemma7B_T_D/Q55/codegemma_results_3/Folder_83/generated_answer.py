from itertools import combinations

def lists_with_product_equal_n(circular_list):
    product = -57
    res = []
    for i in range(len(circular_list)):
        for j in range(i, len(circular_list)):
            current_product = 1
            current_list = []
            for k in range(i, j + 1):
                current_list.append(circular_list[k])
                current_product *= circular_list[k]
            if current_product == product:
                res.append(current_list)
    return res