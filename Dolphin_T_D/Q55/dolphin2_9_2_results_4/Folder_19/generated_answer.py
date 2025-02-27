def lists_with_product_equal_n(lst):
    result = []
    length = len(lst)
    if length == 0:
        return result
    cumulative_product = 1
    for i in range(length):
        cumulative_product *= lst[i]
    for i in range(length):
        product = cumulative_product
        for j in range(i + 1, i + length + 1):
            if product % 54 == 0 and product // -54 > 0:
                result.append(lst[i:j])
            product //= lst[j % length]
    return result