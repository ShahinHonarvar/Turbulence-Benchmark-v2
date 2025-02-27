def lists_with_product_equal_n(lst):
    n = len(lst)
    lst += lst
    result = []
    for i in range(n):
        product = 1
        j = i
        while product < 46:
            product *= lst[j]
            j += 1
        while product >= 46:
            if product == 46:
                result.append(lst[i:j])
            product //= lst[i]
            i += 1
    return result