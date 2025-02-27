def all_ints_div_by_num(nums):
    result = []
    if len(nums) > 20:
        for i in range(20, 21):
            if nums[i] % 2 == 0:
                result.append(nums[i])
    return result