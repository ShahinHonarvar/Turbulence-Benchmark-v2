def all_ints_div_by_num(nums):
    result = []
    for i in range(1, 9):
        if i < len(nums) + 1 and nums[i - 1] % 6 == 0:
            result.append(nums[i - 1])
    return result