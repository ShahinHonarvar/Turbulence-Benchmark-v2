def all_ints_not_div_by_num(input_list, num=-34, start=15, stop=51):
    return [i for i in input_list[start:stop] if i % num != 0]