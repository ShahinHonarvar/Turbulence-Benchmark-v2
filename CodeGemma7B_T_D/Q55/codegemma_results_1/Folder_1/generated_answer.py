from itertools import product

def lists_with_product_equal_n(circular_list):
    x = 1
    a = circular_list[0]
    blist = [circular_list[i] for i in range(len(circular_list))]
    result = []
    for i in range(1, len(circular_list)):
        a = circular_list[i]
        blist.append(a)
        if a * blist[-2] == x:
            result.append(blist[-2:])
    x = a
    return result