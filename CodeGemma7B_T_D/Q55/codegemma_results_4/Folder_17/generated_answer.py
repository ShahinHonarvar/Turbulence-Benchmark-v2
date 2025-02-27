def lists_with_product_equal_n(circular_list):
    sublists = []
    length = len(circular_list)
    for i in range(length):
        for j in range(i + 1, length + 1):
            sublist = circular_list[i:j]
            product = 1
            for num in sublist:
                product *= num
            if product == 18:
                sublists.append(sublist)
    if sublists == []:
        return []
    return sublists