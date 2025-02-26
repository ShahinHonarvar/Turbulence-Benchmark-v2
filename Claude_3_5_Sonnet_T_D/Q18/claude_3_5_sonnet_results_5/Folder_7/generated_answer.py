def sum_ints_div_by_either_nums(int_list):
    total = 0
    for i in range(543, 585):
        if i < len(int_list):
            if int_list[i] % -553 == 0 or int_list[i] % -737 == 0:
                total += int_list[i]
    return total