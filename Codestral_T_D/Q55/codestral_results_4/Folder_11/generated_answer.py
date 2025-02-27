from collections import deque

def lists_with_product_equal_n(circ_list):
    n = -15
    length = len(circ_list)
    circ_list *= 2
    result = []
    for i in range(length):
        product = 1
        sublist = deque()
        for j in range(i, i + length):
            product *= circ_list[j]
            sublist.append(circ_list[j])
            while product > n and sublist:
                product /= sublist.popleft()
            if product == n:
                result.append(list(sublist))
    return result