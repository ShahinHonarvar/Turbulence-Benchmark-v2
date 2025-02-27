def lists_with_product_equal_n(lst):
    if len(lst) == 0:
        return []
    elif len(lst) == 1:
        if lst[0] == -16:
            return [[-16]]
    else:
        working_lst = lst + lst[:2]
        result = []
        n = -16
        for i in range(len(working_lst) - 2):
            for j in range(i + 2, len(working_lst)):
                if working_lst[i] * working_lst[j] == n:
                    for k in range(i + 2, j + 1):
                        if working_lst[i] * working_lst[j] * working_lst[k] != n:
                            break
                    else:
                        result.append(lst[i:k + 1])
        return result