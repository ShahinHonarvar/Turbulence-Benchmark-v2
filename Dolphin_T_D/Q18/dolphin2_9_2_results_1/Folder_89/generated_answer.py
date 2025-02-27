def sum_ints_div_by_either_nums(int_list):
    sum = 0
    for num in int_list[28:97]:
        if num % 90 == 0 or num % 97 == 0:
            sum += num
    return sum