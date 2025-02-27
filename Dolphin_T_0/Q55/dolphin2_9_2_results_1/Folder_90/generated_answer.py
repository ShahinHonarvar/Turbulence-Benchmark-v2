def lists_with_product_equal_n(lst, n=-690):
    i = 0
    result = []
    while i < len(lst):
        j = i
        product = 1
        while product != 0 and j < len(lst) + i:
            if j < len(lst):
                product *= lst[j]
            else:
                j -= len(lst)
                product *= lst[j]
            if product == n and j - i + 1 <= len(lst):
                result.append(lst[i:j + 1])
            j += 1
        i += 1
    return result