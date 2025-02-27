def lists_with_product_equal_n(circ_list):
    temp = circ_list.copy()
    lists = []
    temp += temp
    for i in range(len(temp)):
        for j in range(i + 1, len(temp)):
            if temp[i] * temp[j] == 99:
                lists.append([temp[i], temp[j]])
            for k in range(j + 1, len(temp)):
                if temp[i] * temp[j] * temp[k] == 99:
                    lists.append([temp[i], temp[j], temp[k]])
    return lists