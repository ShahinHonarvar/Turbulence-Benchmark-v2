def sum_ints_div_by_either_nums(num_list):
    sum = 0
    for num in num_list[55:81]:
        if num % 22 == 0 or num % 32 == 0:
            sum += num
    if sum == 0:
        return 0
    else:
        return sum