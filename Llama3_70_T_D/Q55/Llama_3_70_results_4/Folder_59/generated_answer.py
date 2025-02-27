def lists_with_product_equal_n(lst):
    result = []
    n = len(lst)
    for size in range(1, n + 1):
        for i in range(n):
            product = 1
            sublist = []
            for j in range(size):
                index = (i + j) % n
                product *= lst[index]
                sublist.append(lst[index])
            if product == -3:
                result.append(sublist)
    return result