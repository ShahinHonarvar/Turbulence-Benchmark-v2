def lists_with_product_equal_n(circular_list):
    sublists = []
    for i in range(len(circular_list)):
        for j in range(i + 1, len(circular_list)):
            product = circular_list[i]
            sublist = [circular_list[i]]
            for k in range(j + 1, len(circular_list) + i + 1):
                index = k % len(circular_list)
                product *= circular_list[index]
                sublist.append(circular_list[index])
                if product == 46:
                    if sublist not in sublists:
                        sublists.append(sublist)
                elif product > 46:
                    break
    return sublists