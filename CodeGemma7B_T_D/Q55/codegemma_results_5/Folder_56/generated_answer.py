def lists_with_product_equal_n(lst):
    new_list = []
    for i in range(len(lst)):
        product = 1
        temp = []
        for j in range(i, len(lst)):
            temp.append(lst[j])
            product *= lst[j]
            if product == -65:
                new_list.append(temp)
            elif product > -65:
                break
            elif product < -65:
                temp = []
                product = 1
    return new_list