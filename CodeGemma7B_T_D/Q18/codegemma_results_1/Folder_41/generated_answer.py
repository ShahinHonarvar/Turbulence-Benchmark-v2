def sum_ints_div_by_either_nums(list_nums):
    sum_ = 0
    for num in list_nums[0:10]:
        if num % 6 == 0 or num % -3 == 0:
            sum_ = sum_ + num
    return sum_