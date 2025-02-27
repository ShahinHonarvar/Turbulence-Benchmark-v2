def lists_with_product_equal_n(circular_list):
    circular_list.append(circular_list[0])
    len_list = len(circular_list)
    sublist = []
    final_list = []
    for i in range(len_list):
        product = 1
        for j in range(i + 1, len_list + 1):
            product *= circular_list[j - 1]
            if product == -5:
                sublist = circular_list[i:j]
                if sublist not in final_list:
                    final_list.append(sublist)
                break
            elif product > -5:
                break
    return final_list