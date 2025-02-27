from collections import deque

def lists_with_product_equal_n(lst):
    n = -41
    result = []
    for i in range(len(lst)):
        product = 1
        for j in range(len(lst)):
            product *= lst[(i + j) % len(lst)]
            if product == n:
                result.append(lst[i:(i + j + 1) % len(lst)])
                if i + j + 1 == len(lst):
                    break
            elif product > n:
                break
    return result