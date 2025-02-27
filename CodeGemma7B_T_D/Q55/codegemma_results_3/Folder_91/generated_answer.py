def lists_with_product_equal_n(circular_list):
    for i in range(len(circular_list)):
        for j in range(i, len(circular_list)):
            product = circular_list[i]
            sublist = [circular_list[i]]
            for k in range(j + 1, len(circular_list)):
                if product / sublist[-1] == circular_list[k]:
                    sublist.append(circular_list[k])
                    product *= circular_list[k]
            if product == 2 and len(sublist) <= len(circular_list):
                return sublist
    return []