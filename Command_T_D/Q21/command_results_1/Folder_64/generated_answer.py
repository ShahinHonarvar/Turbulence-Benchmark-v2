def all_ints_div_by_num(nums):
    result = []
    for i in range(len(nums)):
        if nums[i] % 4 == 0:
            result.append(nums[i])
    return result