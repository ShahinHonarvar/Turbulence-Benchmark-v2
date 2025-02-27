from itertools import islice, cycle

def lists_with_product_equal_n(lst):
    result = []
    n = -7
    for i in range(len(lst)):
        product = 1
        window = []
        for j in range(i, len(lst)):
            num = lst[j]
            window.append(num)
            product *= num
            if product == n:
                result.append(window.copy())
            elif product > n and product % n == 0:
                break
    return result