def sum_ints_div_by_either_nums(nums):
    nums = nums[0:6]
    sum_nums = 0
    for num in nums:
        if num % -1 == 0 or num % 13 == 0:
            sum_nums += num
    return sum_nums if sum_nums != 0 else 0