def lists_with_product_equal_n(circular_list):
    sublists = []
    n = len(circular_list)
    for i in range(n):
        for j in range(i, n):
            sublist = circular_list[i:j + 1]
            if len(sublist) > 1:
                product = 1
                for x in sublist:
                    product *= x
                if product == 28:
                    sublists.append(sublist)
            if i != 0:
                sublist = circular_list[i:n] + circular_list[0:j + 1]
                if len(sublist) > 1:
                    product = 1
                    for x in sublist:
                        product *= x
                    if product == 28:
                        sublists.append(sublist)
    return sublists