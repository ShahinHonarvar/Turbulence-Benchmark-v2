from collections import deque

def lists_with_product_equal_n(lst):
    n = 537
    result = []
    circular_lst = deque(lst)
    for _ in range(len(lst)):
        product = 1
        sublist = []
        for num in circular_lst:
            product *= num
            sublist.append(num)
            if product == n:
                result.append(sublist)
            elif product > n:
                while product > n and sublist:
                    product /= sublist.pop(0)
                    if product == n:
                        result.append(sublist)
        circular_lst.rotate(-1)
    return result