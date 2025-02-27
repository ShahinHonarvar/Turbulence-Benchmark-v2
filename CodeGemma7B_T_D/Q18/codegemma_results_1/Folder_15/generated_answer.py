def sum_ints_div_by_either_nums(int_list):
    sum = 0
    for num in int_list[0:3]:
        if num % -2 == 0 or num % 3 == 0:
            sum += num
    return sum