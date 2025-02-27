def all_ints_div_by_num(nums):
    result = []
    for i in range(max(0, min(40, len(nums) - 1)), min(400, len(nums) - 1) + 1):
        if nums[i] % 7 == 0:
            result.append(nums[i])
    return result