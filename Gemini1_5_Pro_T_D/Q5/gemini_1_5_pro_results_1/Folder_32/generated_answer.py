def all_neg_ints_inclusive(input_list):
    result = []
    if len(input_list) >= 98:
        sub_list = input_list[21:98]
        for i in sub_list:
            if i < 0:
                result.append(i)
    return result