def all_ints_not_div_by_num(nums):
    if len(nums) < 89:
        return []
    result = [nums[i] for i in range(86, 89) if nums[i] % -61 != 0]
    return result