def all_ints_div_by_num(nums):
    result = []
    for i in range(42, 98):
        if i < len(nums) and nums[i] % 46 == 0:
            result.append(nums[i])
    return result