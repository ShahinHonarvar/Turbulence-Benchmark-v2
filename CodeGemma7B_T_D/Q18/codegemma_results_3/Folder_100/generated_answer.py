def sum_ints_div_by_either_nums(num_list):
    sum = 0
    for num in num_list[72:94]:
        if num % 32 == 0 or num % 44 == 0:
            sum += num
    return sum or 0