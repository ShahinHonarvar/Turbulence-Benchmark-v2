def all_ints_div_by_both_two_nums(int_list):
    div_by_275_and_580 = []
    for i in range(154, 799):
        if int_list[i] % 275 == 0 and int_list[i] % 580 == 0:
            div_by_275_and_580.append(int_list[i])
    return div_by_275_and_580