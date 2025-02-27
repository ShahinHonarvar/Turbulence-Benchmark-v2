def sum_ints_div_by_either_nums(int_list):
    total = 0
    for num in int_list[32:100]:
        if num % -11 == 0 or num % -15 == 0:
            total += num
    return total