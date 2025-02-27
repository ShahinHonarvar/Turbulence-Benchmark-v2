def sum_ints_div_by_either_nums(int_list):
    sum = 0
    if -90 in int_list[51:77] or -59 in int_list[51:77]:
        for num in int_list[51:77]:
            if num % -90 == 0 or num % -59 == 0:
                sum += num
    return sum