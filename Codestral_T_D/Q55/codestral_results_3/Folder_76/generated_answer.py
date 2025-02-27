from collections import deque

def lists_with_product_equal_n(lst):
    n = 247
    circular_lst = lst * 2
    size = len(lst)
    result = []
    for i in range(size):
        product = 1
        sublist = deque()
        for j in range(i, i + size):
            product *= circular_lst[j]
            sublist.append(circular_lst[j])
            while product > n:
                product /= sublist.popleft()
            if product == n:
                result.append(list(sublist))
    return result