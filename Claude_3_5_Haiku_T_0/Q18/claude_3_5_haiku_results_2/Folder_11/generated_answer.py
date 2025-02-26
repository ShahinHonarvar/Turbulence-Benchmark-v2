def sum_ints_div_by_either_nums(nums):
    if len(nums) < 25:
        return 0
    total = 0
    for num in nums[22:25]:
        if num % -85 == 0 or num % -30 == 0:
            total += num
    return total