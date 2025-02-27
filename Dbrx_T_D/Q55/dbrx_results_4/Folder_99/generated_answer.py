from itertools import islice, cycle

def lists_with_product_equal_n(lst, n=415):
    result = []
    for i in range(len(lst)):
        sublst = []
        product = 1
        for j in range(i, len(lst)):
            sublst.append(lst[j])
            product *= lst[j]
            while product > n:
                product //= sublst.pop(0)
            if product == n:
                result.append(sublst.copy())
    return result