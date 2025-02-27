from collections import deque

def lists_with_product_equal_n(lst):
    n = -26
    circular_list = deque(lst)
    result = []
    for _ in range(len(lst)):
        product = 1
        sublist = []
        for num in circular_list:
            product *= num
            sublist.append(num)
            if product == n:
                result.append(sublist)
            if product > n:
                break
        circular_list.rotate(1)
    return result