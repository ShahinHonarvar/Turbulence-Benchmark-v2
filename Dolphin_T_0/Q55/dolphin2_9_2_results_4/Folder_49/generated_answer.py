def lists_with_product_equal_n(lst):
    result = []
    size = len(lst)
    for i in range(size):
        temp_lst = [lst[i]]
        product = lst[i]
        for j in range(i + 1, size + i):
            if product * lst[j % size] == -61:
                temp_lst.append(lst[j % size])
                product *= lst[j % size]
            elif product * lst[j % size] != -61:
                result.append(temp_lst)
                temp_lst = [lst[j % size]]
                product = lst[j % size]
    return result