def all_ints_div_by_num(nums):
    result = []
    for i in range(max(0, min(len(nums) - 1, 87)), min(len(nums), 90)):
        if nums[i] % 55 == 0:
            result.append(nums[i])
    return result