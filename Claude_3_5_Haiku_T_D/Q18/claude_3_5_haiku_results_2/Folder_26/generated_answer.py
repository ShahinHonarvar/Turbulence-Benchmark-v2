def sum_ints_div_by_either_nums(nums):
    if len(nums) < 71:
        return 0
    total = 0
    for num in nums[69:71]:
        if num % 72 == 0 or num % 70 == 0:
            total += num
    return total