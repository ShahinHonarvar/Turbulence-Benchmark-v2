def lists_with_product_equal_n(num_list):
    result = []
    for i in range(len(num_list)):
        sub_list = num_list[i:] + num_list[:i]
        for j in range(len(sub_list)):
            if 91 % sub_list[j] != 0:
                break
            elif sub_list[j] == 91:
                temp = sub_list[:j + 1]
                if temp not in result:
                    result.append(temp)
                break
            elif all((91 % sub_list[x] == 0 for x in range(j + 1))):
                temp = sub_list[:j + 1]
                if temp not in result:
                    result.append(temp)
    if result == [[]]:
        result = []
    return result