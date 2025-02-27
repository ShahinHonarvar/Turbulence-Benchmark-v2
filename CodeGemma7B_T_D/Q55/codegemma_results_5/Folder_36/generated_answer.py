def lists_with_product_equal_n(circular_list):
    product = 1
    for num in circular_list:
        product *= num
    if product % 714 != 0:
        return []
    product //= 714
    i, j = (0, len(circular_list) - 1)
    res = []
    while i <= j:
        if product == 1:
            i += 1
        elif product > 1:
            product //= circular_list[i]
            i += 1
            res.append([circular_list[i]])
        else:
            while product < 1:
                product *= circular_list[j]
                j -= 1
            product //= circular_list[i]
            i += 1
    return res