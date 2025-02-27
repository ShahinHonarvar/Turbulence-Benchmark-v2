from itertools import islice

def lists_with_product_equal_n(circular_list):
    n = 733
    result = []
    for i in range(len(circular_list)):
        sub_list = list(islice(circular_list, i, i + len(circular_list) - 1))
        if sub_list and sub_list[-1] * (sub_list[0] or 1) == n:
            result.append(sub_list)
    return result