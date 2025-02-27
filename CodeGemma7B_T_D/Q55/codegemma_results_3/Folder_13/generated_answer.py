def lists_with_product_equal_n(circular_list):
    lists = []
    for i in range(1, len(circular_list)):
        for j in range(i + 1, len(circular_list)):
            product = circular_list[i] * circular_list[j]
            sublist = [circular_list[i], circular_list[j]]
            for k in range(j + 1, len(circular_list)):
                if circular_list[k] * product == 54:
                    sublist.append(circular_list[k])
                    product *= circular_list[k]
            if product == 54 and sublist not in lists:
                lists.append(sublist)
    return lists