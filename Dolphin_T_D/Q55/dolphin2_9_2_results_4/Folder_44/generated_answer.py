def lists_with_product_equal_n(lst):
    result = []
    length = len(lst)
    for i in range(length):
        product = 1
        for j in range(i, i + length):
            product *= lst[j % length]
            if product == 29:
                temp = []
                for k in range(i, j + 1):
                    temp.append(lst[k % length])
                result.append(temp)
    return result