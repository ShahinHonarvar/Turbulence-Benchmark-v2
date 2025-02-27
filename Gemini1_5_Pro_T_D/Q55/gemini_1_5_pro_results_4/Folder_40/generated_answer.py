def lists_with_product_equal_n(circular_list):
    n = -9
    result = []
    length = len(circular_list)
    for i in range(length):
        for j in range(i, i + length):
            sublist = circular_list[i:j % length] + circular_list[j % length:] + circular_list[:j % length]
            for k in range(len(sublist)):
                for l in range(k + 1, len(sublist) + 1):
                    if len(sublist[k:l]) <= length and reduce(lambda x, y: x * y, sublist[k:l]) == n:
                        result.append(sublist[k:l])
    return result