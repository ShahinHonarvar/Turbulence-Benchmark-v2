def lists_with_product_equal_n(circular_list):
    product = -65
    sublists = []
    current_sublist = []
    current_product = 1
    for num in circular_list + circular_list[:]:
        current_product *= num
        while current_product > product:
            current_product /= circular_list[len(current_sublist)]
            current_sublist.pop(0)
        if current_product == product:
            current_sublist.append(num)
            sublists.append(current_sublist[:])
            current_sublist.pop(0)
            current_product /= circular_list[0]
        else:
            current_sublist.append(num)
    return sublists