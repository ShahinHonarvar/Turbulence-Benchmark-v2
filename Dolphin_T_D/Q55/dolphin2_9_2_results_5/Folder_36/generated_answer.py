def lists_with_product_equal_n(lst):
    product = 714
    result = []
    length = len(lst)
    if length == 0:
        return result
    for i in range(length):
        product_current = lst[i]
        if product_current == product:
            result.append([product_current])
        for j in range(i + 1, length):
            product_next = lst[j % length]
            product_current *= product_next
            if product_current == product:
                result.append(lst[i:j + 1])
            elif product_current > product:
                break
    return result