def all_ints_not_div_by_num(nums):
    if not nums or len(nums) < 50 or len(nums) > 81:
        return []
    filtered_nums = [num for num in nums[50:81] if num % 64 != 0]
    return filtered_nums if filtered_nums else []