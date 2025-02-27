from functools import reduce

def lists_with_product_equal_n(circ):
    i = 0
    lists = []
    for k in range(len(circ)):
        product = reduce(lambda a, b: a * b, circ[i:k + 1])
        if product == 990:
            lists.append(circ[i:k + 1])
        if product > 990:
            i = k + 1
    return lists