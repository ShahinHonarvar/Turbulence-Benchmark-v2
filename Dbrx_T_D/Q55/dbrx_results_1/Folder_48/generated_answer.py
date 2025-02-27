from itertools import islice, cycle

def lists_with_product_equal_n(lst):
    n = 990
    result = []
    for i in range(len(lst)):
        sub_product = 1
        for j in range(i, len(lst)):
            sub_product *= lst[j]
            if sub_product == n:
                result.append(lst[i:j + 1])
            elif sub_product > n:
                break
    return result[::-1]