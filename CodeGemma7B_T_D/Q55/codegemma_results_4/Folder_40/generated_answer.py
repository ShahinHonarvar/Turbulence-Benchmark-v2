from itertools import tee

def lists_with_product_equal_n(circular_list):
    n = 9
    lists = []
    iter1, iter2 = tee(circular_list)
    next(iter2)
    for i, sublist in enumerate(zip(iter1, iter2)):
        product = sublist[0] * sublist[1]
        if product == n:
            lists.append([circular_list[i], circular_list[i + 1]])
    for i in range(len(circular_list) - 2):
        product = circular_list[i] * circular_list[i + 1] * circular_list[i + 2]
        if product == n:
            lists.append([circular_list[i], circular_list[i + 1], circular_list[i + 2]])
    return lists