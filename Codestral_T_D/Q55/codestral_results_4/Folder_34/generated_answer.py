from itertools import cycle, islice

def lists_with_product_equal_n(lst):
    n = -81
    result = []
    for i in range(len(lst)):
        prod = 1
        temp = []
        for j in islice(cycle(lst), i, i + len(lst)):
            prod *= j
            temp.append(j)
            if prod == n:
                result.append(temp)
            if abs(prod) > abs(n):
                break
    return result