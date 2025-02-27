def all_ints_not_div_by_num(input_list):
    for i in range(len(input_list)):
        if i >= 48 and i < 62:
            if input_list[i] % 28 == 0:
                input_list[i] = float('NaN')
    return [x for x in input_list if x == int(x) and x % 28 != 0 and (x == x)]