def all_ints_div_by_num(nums):
    result = []
    for i in range(10, 53):
        if i < len(nums) and nums[i] % -12 == 0:
            result.append(nums[i])
    return result