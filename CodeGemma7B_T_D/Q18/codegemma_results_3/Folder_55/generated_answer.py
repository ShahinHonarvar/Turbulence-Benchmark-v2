def sum_ints_div_by_either_nums(int_list):
    sum = 0
    for num in int_list[0:10]:
        if num % 10 == 0 or num % 100 == 0:
            sum += num
    return sum