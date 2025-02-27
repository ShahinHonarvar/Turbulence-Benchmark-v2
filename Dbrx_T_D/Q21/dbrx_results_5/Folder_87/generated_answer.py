def all_ints_div_by_num(nums):
    result = []
    for i in range(len(nums)):
        if i >= 10 and i <= 56 and (nums[i] % 16 == 0):
            result.append(nums[i])
    return result