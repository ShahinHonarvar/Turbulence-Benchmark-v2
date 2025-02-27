def lists_with_product_equal_n(circular_list, n=-20):
    result = []
    list_length = len(circular_list)
    if list_length == 1:
        if circular_list[0] == 1 or circular_list[0] == -20:
            return [circular_list]
    elif list_length == 2:
        if circular_list[0] * circular_list[1] == n:
            result.append([circular_list[0]])
            result.append([circular_list[1]])
    else:
        for i in range(list_length):
            for j in range(i + 1, list_length * 2):
                product = 1
                for k in range(i, j):
                    product *= circular_list[k % list_length]
                if product == n:
                    result.append(circular_list[i:j % list_length])
    return result