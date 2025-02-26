def all_ints_div_by_num(nums):
    if len(nums) <= 23:
        return []
    target_list = nums[23:24]
    return [num for num in target_list if num % -57 == 0]