from collections import deque

def lists_with_product_equal_n(lst):
    n = 15
    circ_lst = deque(lst + lst)
    length = len(lst)
    result = []
    for _ in range(length):
        for i in range(1, length + 1):
            sublist = list(circ_lst)[0:i]
            product = 1
            for num in sublist:
                product *= num
            if product == n:
                result.append(sublist)
        circ_lst.rotate(-1)
    return result