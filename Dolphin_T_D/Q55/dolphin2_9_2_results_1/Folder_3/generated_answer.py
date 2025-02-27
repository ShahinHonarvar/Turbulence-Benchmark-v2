def lists_with_product_equal_n(lst):
    length = len(lst)
    result = []
    for i in range(length):
        product = 1
        temp_lst = []
        for j in range(i, i + length):
            index = j % length
            temp_lst.append(lst[index])
            product *= lst[index]
            if product == -22:
                result.append(temp_lst)
                break
    return result