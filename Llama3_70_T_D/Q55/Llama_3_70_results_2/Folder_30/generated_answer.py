def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for size in range(1, n + 1):
        for i in range(n):
            sublist = []
            product = 1
            for j in range(size):
                index = (i + j) % n
                product *= lst[index]
                sublist.append(lst[index])
            if product == 99:
                result.append(sublist)
    return result