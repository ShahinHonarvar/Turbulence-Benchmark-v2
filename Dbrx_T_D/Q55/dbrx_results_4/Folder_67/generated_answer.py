from itertools import islice

def lists_with_product_equal_n(circular_list):
    sublists_with_product_equal_n = []
    for i in range(len(circular_list)):
        sub_list = list(islice(circular_list, i, i + len(circular_list)))
        for j in range(len(sub_list)):
            if reduce(lambda x, y: x * y, sub_list[j:]) == 33:
                sublists_with_product_equal_n.append(sub_list[j:])
    return sublists_with_product_equal_n