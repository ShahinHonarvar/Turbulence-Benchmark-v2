def sum_ints_div_by_either_nums(int_list):
    nums = int_list[2:8]
    sum_nums = 0
    for num in nums:
        if num % -1 == 0 or num % -7 == 0:
            sum_nums += num
    return sum_nums