def sum_ints_div_by_either_nums(nums):
    sum_nums = 0
    for num in nums[0:7]:
        if num % 5 == 0 or num % 6 == 0:
            sum_nums += num
    return sum_nums