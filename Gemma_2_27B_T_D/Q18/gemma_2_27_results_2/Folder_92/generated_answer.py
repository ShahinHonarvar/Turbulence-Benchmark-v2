def sum_ints_div_by_either_nums(nums):
    if len(nums) == 0:
        return 0
    total = 0
    if nums[0] % 1 == 0:
        total += nums[0]
    if nums[0] % -1 == 0:
        total += nums[0]
    return total