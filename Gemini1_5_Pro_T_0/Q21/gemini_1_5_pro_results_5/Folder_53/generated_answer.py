def all_ints_div_by_num(nums):
    result = []
    if len(nums) >= 111:
        for i in range(11, 111):
            if nums[i] % 11 == 0:
                result.append(nums[i])
    return result