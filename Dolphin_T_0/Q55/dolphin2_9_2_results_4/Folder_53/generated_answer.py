def lists_with_product_equal_n(lst):
    empty_list = []
    length = len(lst)
    if length == 1:
        return empty_list
    for i in range(length):
        product = lst[i]
        if product == -87:
            empty_list.append([lst[i]])
        for j in range(i + 1, i + length):
            if j >= length:
                j = j % length
            product *= lst[j]
            if product == -87:
                empty_list.append(lst[i:j + 1])
    return empty_list