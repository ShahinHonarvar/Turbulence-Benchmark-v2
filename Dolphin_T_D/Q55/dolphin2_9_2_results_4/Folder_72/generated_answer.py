def lists_with_product_equal_n(lst):
    result = []
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            sub_list = lst[i:j + 1]
            if (sub_list[-1] + sub_list[0]) % 10 == 0:
                result.append(sub_list)
    return result