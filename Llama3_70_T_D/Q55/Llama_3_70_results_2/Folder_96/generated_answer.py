def lists_with_product_equal_n(lst):
    result = []
    length = len(lst)
    for i in range(length):
        for j in range(1, length + 1):
            if 0 in lst[i:i + j]:
                product = 1
                for num in lst[i:i + j]:
                    product *= num
                if product == 0:
                    sublist = lst[i:i + j]
                    if i + j > length:
                        sublist += lst[:i + j - length]
                    result.append(sublist)
    return result