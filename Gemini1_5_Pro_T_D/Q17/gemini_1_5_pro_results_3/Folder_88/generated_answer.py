def all_ints_div_by_both_two_nums(nums):
    result = []
    for i in range(max(3, 0), min(10, len(nums))):
        if nums[i] % 6 == 0 and nums[i] % 1 == 0:
            result.append(nums[i])
    return result