from collections import deque

def lists_with_product_equal_n(lst):
    n = len(lst)
    lst = deque(lst * 2)
    result = []
    for i in range(n):
        for j in range(i + 1, i + n):
            if i <= j:
                sublist = list(lst)[i:j]
                product = 1
                for num in sublist:
                    product *= num
                if product == 54:
                    result.append(sublist)
            else:
                sublist = list(lst)[i:] + list(lst)[:j]
                product = 1
                for num in sublist:
                    product *= num
                if product == 54:
                    result.append(sublist)
    return result