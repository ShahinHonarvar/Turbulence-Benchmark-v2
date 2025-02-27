from itertools import islice

def lists_with_product_equal_n(circular_list):
    result = []
    for i in range(len(circular_list)):
        sub_list = list(islice(circular_list, i, i + len(circular_list)))
        if sub_list[0] * sub_list[1:] == -15:
            result.append(sub_list)
    return result