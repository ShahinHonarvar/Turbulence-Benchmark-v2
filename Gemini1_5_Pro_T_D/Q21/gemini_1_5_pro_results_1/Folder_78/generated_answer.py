def all_ints_div_by_num(nums):
    result = []
    for i in range(max(0, min(len(nums) - 1, 57)), min(len(nums), 68)):
        if nums[i] % 90 == 0:
            result.append(nums[i])
    return result