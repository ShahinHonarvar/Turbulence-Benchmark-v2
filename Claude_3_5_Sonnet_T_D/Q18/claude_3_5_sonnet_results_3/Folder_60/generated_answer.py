def sum_ints_div_by_either_nums(integer_list):
    total = 0
    for num in integer_list[10:80]:
        if num % -74 == 0 or num % -58 == 0:
            total += num
    return total