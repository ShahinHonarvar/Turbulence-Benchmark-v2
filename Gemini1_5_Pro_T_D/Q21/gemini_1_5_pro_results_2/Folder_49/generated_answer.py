def all_ints_div_by_num(nums):
    result = []
    for i in range(30, 301):
        if i < len(nums) and nums[i] % 5 == 0:
            result.append(nums[i])
    return result