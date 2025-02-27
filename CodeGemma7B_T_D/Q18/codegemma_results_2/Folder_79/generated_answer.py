def sum_ints_div_by_either_nums(nums):
    sum_divisible = 0
    for num in nums[8:10]:
        if num % 3 == 0 or num % 6 == 0:
            sum_divisible += num
    return sum_divisible or 0