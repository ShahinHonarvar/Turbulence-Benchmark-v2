def sum_ints_div_by_either_nums(int_list):
    total = 0
    for num in int_list[50:201]:
        if num % -34 == 0 or num % 64 == 0:
            total += num
    return total