def all_ints_div_by_num(nums):
    result = []
    if len(nums) > 10:
        for i in range(10, 11):
            if nums[i] % 1 == 0:
                result.append(nums[i])
    return result