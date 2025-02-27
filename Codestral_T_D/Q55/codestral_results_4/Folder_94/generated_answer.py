def lists_with_product_equal_n(lst):
    length = len(lst)
    lst += lst
    result = []
    for i in range(length):
        current_product = 1
        for j in range(i, i + length):
            current_product *= lst[j]
            if current_product == -30:
                result.append(lst[i:j + 1])
            if current_product == 0:
                break
    return result