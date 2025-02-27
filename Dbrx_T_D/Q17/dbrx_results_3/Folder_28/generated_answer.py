def all_ints_div_by_both_two_nums(input_list):
    div_by_27_57 = []
    for i in input_list[34:82]:
        if i % 27 == 0 and i % 57 == 0:
            div_by_27_57.append(i)
    return div_by_27_57