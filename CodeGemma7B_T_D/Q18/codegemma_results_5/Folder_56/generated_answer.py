def sum_ints_div_by_either_nums(num_list):
    sum = 0
    for num in num_list[7:10]:
        if num % 9 == 0 or num % 7 == 0:
            sum += num
    if sum == 0:
        return 0
    else:
        return sum