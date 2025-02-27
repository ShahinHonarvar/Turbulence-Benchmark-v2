def lists_with_product_equal_n(circular_list, n=-22):
    product = 1
    for i in range(len(circular_list)):
        product *= circular_list[i]
    if product != n:
        return []
    sublists = []
    for n in range(1, len(circular_list)):
        for i in range(len(circular_list)):
            sublist = []
            for j in range(i, i + n):
                sublist.append(circular_list[j])
                product = 1
                for item in sublist:
                    product *= item
                if product == n:
                    sublists.append(sublist)
    return sublists