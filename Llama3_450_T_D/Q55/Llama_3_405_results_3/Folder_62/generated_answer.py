def lists_with_product_equal_n(lst):
    result = []
    length = len(lst)
    for i in range(length):
        product = 1
        for j in range(i, i + length):
            product *= lst[j % length]
            if product == 100:
                sublist = [lst[k % length] for k in range(i, j + 1)]
                result.append(sublist)
            elif product > 100:
                break
    return result