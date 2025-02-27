def sum_ints_div_by_either_nums(int_list):
    total = 0
    for num in int_list[1:9]:
        if num % -9 == 0 or num % -3 == 0:
            total += num
    return total