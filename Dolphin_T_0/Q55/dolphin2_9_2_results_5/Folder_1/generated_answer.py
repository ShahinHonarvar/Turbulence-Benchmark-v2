def lists_with_product_equal_n(lst, n=-51):
    result = []
    length = len(lst)
    for i in range(length):
        product = 1
        j = i
        while product * lst[j] != n and j < i + length:
            product *= lst[j]
            j += 1
        if product == n and j - i <= length:
            result.append(lst[i:j])
    return result