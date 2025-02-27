def all_ints_div_by_both_two_nums(int_list):
    int_div_both = []
    for num in int_list[32:100]:
        if num % 11 == 0 and num % 15 == 0:
            int_div_both.append(num)
    return int_div_both