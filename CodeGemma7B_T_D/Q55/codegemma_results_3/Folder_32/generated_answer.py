def lists_with_product_equal_n(circular_list):
    circular_list += circular_list
    prefix_products = []
    result = []
    for i in range(len(circular_list)):
        for j in range(i, len(circular_list)):
            prefix_products.append(circular_list[i] * circular_list[i + 1] * ... * circular_list[j])
    for i, product in enumerate(prefix_products):
        if product == 76:
            sublist = [circular_list[i]]
            j = i + 1
            while j < len(prefix_products) and prefix_products[j] != sublist[-1] * circular_list[j]:
                sublist.append(circular_list[j])
                j += 1
            result.append(sublist)
    for i, product in enumerate(prefix_products):
        if product == 76:
            sublist = [circular_list[i]]
            j = i + 1
            while j < len(prefix_products) and prefix_products[j] != sublist[-1] * circular_list[j]:
                sublist.append(circular_list[j])
                j += 1
            if sublist in result:
                continue
            extended_index = circular_list.index(sublist[0])
            for j in range(extended_index + 1, len(circular_list)):
                if circular_list[j] == sublist[-1] * circular_list[j - sublist[-1]]:
                    sublist.append(circular_list[j])
            result.append(sublist)
    return result