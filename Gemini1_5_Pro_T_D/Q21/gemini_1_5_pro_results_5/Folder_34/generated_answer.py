def all_ints_div_by_num(nums):
    result = []
    if len(nums) > 30:
        for i in range(30, 31):
            if nums[i] % 3 == 0:
                result.append(nums[i])
    return result