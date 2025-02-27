def lists_with_product_equal_n(lst):
    n = -22
    size = len(lst)
    lst += lst
    result = []
    for i in range(size):
        product = 1
        for j in range(i, size + i):
            product *= lst[j]
            if product == n:
                result.append(lst[i:j + 1])
            while product % n == 0 and i < j:
                product //= lst[i]
                i += 1
                if product == n:
                    result.append(lst[i:j + 1])
    return result