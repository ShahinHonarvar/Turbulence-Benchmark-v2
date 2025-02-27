def all_ints_div_by_num(nums):
    result = [nums[i] for i in range(len(nums)) if i >= 62 and i <= 63 and (nums[i] % 99 == 0)]
    return result