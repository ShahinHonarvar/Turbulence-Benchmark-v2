def lists_with_product_equal_n(lst):
    product = -72
    temp = []
    result = []
    i = 0
    while i < len(lst):
        temp.append(lst[i])
        temp_product = 1
        for number in temp:
            temp_product *= number
        if temp_product == product and len(temp) <= len(lst):
            result.append(temp[:])
        if temp_product != product or i == len(lst) - 1:
            temp.pop(0)
        i += 1
    return result