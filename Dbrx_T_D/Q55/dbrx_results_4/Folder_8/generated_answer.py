from itertools import islice, chain

def sub_lists_circular(lst):
    length = len(lst)
    sublists = []
    for i in range(length):
        for j in range(i + 1, length + i - 1):
            head, tail = (j % length, (j + 1) % length)
            sublists.append(lst[head:tail])
    return sublists

def is_product_n(lst, n):
    if not lst:
        return False
    product = 1
    for i in range(len(lst)):
        product *= lst[i]
        if product == n:
            return True
        elif product > n:
            break
    return False

def lists_with_product_equal_n(lst, n):
    sublists = sub_lists_circular(lst)
    result = [sublist for sublist in sublists if is_product_n(sublist, n)]
    return result