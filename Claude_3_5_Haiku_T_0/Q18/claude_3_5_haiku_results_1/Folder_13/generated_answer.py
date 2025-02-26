def sum_ints_div_by_either_nums(nums):
    total = 0
    for num in nums[13:19]:
        if num % 45 == 0 or num % 20 == 0:
            total += num
    return total