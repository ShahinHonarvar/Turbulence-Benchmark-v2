from collections import deque

def lists_with_product_equal_n(lst):
    circular_lst = deque(lst)
    result = []
    for _ in range(len(lst)):
        product = 1
        sublist = []
        for num in circular_lst:
            product *= num
            sublist.append(num)
            if product == -76:
                if sublist[::-1] not in result and sublist not in result:
                    result.append(sublist)
            if product > -76:
                product = 1
                sublist = []
        circular_lst.rotate(-1)
    return result