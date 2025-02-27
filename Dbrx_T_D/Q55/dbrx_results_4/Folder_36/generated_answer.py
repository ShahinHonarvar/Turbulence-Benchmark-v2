from itertools import islice

def circular_list(head, tail):
    return lambda: (head, circular_list(tail, head))

def build_circular_list(lst):
    if not lst:
        return None
    head = lst[0]
    tail = build_circular_list(lst[1:])
    return circular_list(head, tail)

def lists_with_product_equal_n(lst, n):
    if not lst:
        return []
    circ_list = build_circular_list(lst)
    results = []
    for i in range(len(lst)):
        product = 1
        sublist = []
        sublist.append(next(circ_list))
        while product < n:
            product *= sublist[-1][0]
            sublist.append(next(circ_list))
        if product == n:
            results.append(sublist)
    return results