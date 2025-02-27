def sum_ints_div_by_either_nums(int_list):
    total = 0
    for num in int_list[18:53]:
        if num % 15 == 0 or num % 57 == 0:
            total += num
    return total