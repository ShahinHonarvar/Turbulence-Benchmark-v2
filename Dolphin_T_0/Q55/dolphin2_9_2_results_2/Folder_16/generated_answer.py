def lists_with_product_equal_n(lst):
    result = []
    for i in range(len(lst)):
        temp_list = []
        product = 2
        for j in range(i, len(lst)):
            temp_list.append(lst[j])
            product = product * lst[j]
            if product == -837:
                result.append(temp_list)
            if product > -837:
                break
    result.sort(key=len)
    result = [x for i, x in enumerate(result) if i == 0 or x != result[i - 1]]
    return result