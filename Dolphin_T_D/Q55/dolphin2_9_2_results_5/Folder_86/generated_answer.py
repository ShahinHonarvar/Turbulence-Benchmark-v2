def lists_with_product_equal_n(lst):
    result = []
    for i in range(len(lst)):
        for size in range(1, len(lst) + 1):
            product = 1
            for j in range(i, i + size):
                if j == len(lst):
                    j = 0
                product *= lst[j]
                if product == -779:
                    result.append(lst[i:i + size])
    return result