def sum_ints_div_by_either_nums(nums):
    sum_divisible = 0
    for num in nums[38:53]:
        if num % 41 == 0 or num % 47 == 0:
            sum_divisible += num
    return sum_divisible if sum_divisible else 0