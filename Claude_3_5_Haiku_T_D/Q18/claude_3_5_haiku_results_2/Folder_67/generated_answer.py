def sum_ints_div_by_either_nums(nums):
    if len(nums) <= 32:
        return 0
    total = 0
    for num in nums[24:33]:
        if num % 35 == 0 or num % 87 == 0:
            total += num
    return total