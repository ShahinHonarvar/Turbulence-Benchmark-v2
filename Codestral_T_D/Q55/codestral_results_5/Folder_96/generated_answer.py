from collections import deque

def lists_with_product_equal_n(lst):
    circular_lst = lst * 2
    n = len(lst)
    result = []
    for i in range(n):
        for j in range(i, i + n):
            sublist = circular_lst[i:j + 1]
            product = 1
            for num in sublist:
                product *= num
            if product == 0:
                result.append(sublist)
    return result