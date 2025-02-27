from collections import deque

def lists_with_product_equal_n(circular_list):
    circular_list = deque(circular_list)
    n = -65
    result = []
    for _ in range(len(circular_list)):
        product = 1
        sublist = []
        for num in circular_list:
            product *= num
            sublist.append(num)
            if product == n:
                result.append(sublist)
            while product > n and len(sublist) > 1:
                product /= sublist.pop(0)
                if product == n:
                    result.append(sublist)
        circular_list.rotate(-1)
    return result