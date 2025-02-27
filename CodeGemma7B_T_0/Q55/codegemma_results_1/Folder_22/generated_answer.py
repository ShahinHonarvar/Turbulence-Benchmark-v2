def lists_with_product_equal_n(circular_list):
    sublists = []
    for i in range(len(circular_list)):
        for j in range(i + 1, len(circular_list)):
            product = circular_list[i]
            sublist = [circular_list[i]]
            for k in range(j + 1, len(circular_list)):
                product *= circular_list[k]
                sublist.append(circular_list[k])
                if product == 4:
                    sublists.append(sublist[:])
    return sublists