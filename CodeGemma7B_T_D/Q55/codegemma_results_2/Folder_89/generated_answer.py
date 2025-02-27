def lists_with_product_equal_n(circular_list, n=57):
    sublists = []
    current_sublist = []
    current_product = 1
    for i in range(len(circular_list)):
        current_sublist.append(circular_list[i])
        current_product *= circular_list[i]
        while current_product > n:
            current_product //= current_sublist[0]
            current_sublist.pop(0)
        if current_product == n:
            sublists.append(current_sublist[:])
            current_sublist.clear()
            current_product = 1
    return sublists