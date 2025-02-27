def sum_ints_div_by_either_nums(int_list):
    total = 0
    for i in range(61, 89):
        if int_list[i] % 31 == 0 or int_list[i] % 11 == 0:
            total += int_list[i]
    return total if total != 0 else None