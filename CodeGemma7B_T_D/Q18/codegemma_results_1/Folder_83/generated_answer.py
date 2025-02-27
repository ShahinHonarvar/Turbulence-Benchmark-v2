def sum_ints_div_by_either_nums(num_list):
    sum_of_nums = 0
    for num in num_list[90:201]:
        if num % 31 == 0 or num % 13 == 0:
            sum_of_nums += num
    return sum_of_nums if sum_of_nums else 0