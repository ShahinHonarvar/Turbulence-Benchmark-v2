def all_ints_div_by_both_two_nums(int_list):
    new_list = []
    for num in int_list[55:85]:
        if num % -24 == 0 and num % -11 == 0:
            new_list.append(num)
    return new_list