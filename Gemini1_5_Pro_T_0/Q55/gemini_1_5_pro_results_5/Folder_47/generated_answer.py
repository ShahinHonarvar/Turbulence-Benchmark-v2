def lists_with_product_equal_n(circular_list):
    n = -94
    result = []
    for i in range(len(circular_list)):
        for j in range(i, len(circular_list)):
            sublist = circular_list[i:j + 1]
            if j + 1 - i < len(circular_list):
                sublist.extend(circular_list[:j + 1 - i - len(circular_list)])
            if len(sublist) > 0:
                product = 1
                for k in range(len(sublist)):
                    product *= sublist[k]
                if product == n:
                    result.append(sublist)
    return result