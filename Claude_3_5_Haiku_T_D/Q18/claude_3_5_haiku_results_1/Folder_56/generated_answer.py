def sum_ints_div_by_either_nums(nums):
    if len(nums) < 10:
        return 0
    sum_divisible = 0
    for num in nums[7:10]:
        if num % -9 == 0 or num % -7 == 0:
            sum_divisible += num
    return sum_divisible