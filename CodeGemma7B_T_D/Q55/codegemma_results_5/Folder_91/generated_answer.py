def lists_with_product_equal_n(circular_list):
    product_two = 2
    length = len(circular_list)
    sublists = []
    for i in range(length):
        sublist = [circular_list[i]]
        j = (i + 1) % length
        while product_two == circular_list[i] * circular_list[j]:
            sublist.append(circular_list[j])
            j = (j + 1) % length
            if len(sublist) > length:
                break
        if sublist and len(sublist) <= length:
            sublists.append(sublist)
    return sublists