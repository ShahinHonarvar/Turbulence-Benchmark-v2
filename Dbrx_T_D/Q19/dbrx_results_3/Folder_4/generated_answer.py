def all_ints_not_div_by_num(input_list):
    for i in range(len(input_list)):
        if i >= 19 and i < 49 and (input_list[i] % -36 != 0):
            yield input_list[i]
        elif i >= 19 and i < 49:
            continue
        elif i >= 49:
            break