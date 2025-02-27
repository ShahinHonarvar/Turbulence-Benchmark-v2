def lists_with_product_equal_n(circular_list):
    n = 632
    circular_list.extend(circular_list)
    for i in range(len(circular_list) - 1):
        for j in range(i + 1, len(circular_list)):
            product = circular_list[i]
            for k in range(j, len(circular_list)):
                if circular_list[k] != 0 and product % circular_list[k] == 0:
                    product //= circular_list[k]
                    sublist = []
                    for l in range(i, k + 1):
                        sublist.append(circular_list[l])
                    if product == 1:
                        result.append(sublist)
    result = list(set(map(tuple, result)))
    return result