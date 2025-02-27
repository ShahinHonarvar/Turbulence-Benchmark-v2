def all_ints_not_div_by_num(nums):
    filtered_nums = [num for num in nums[14:21] if num % -93 != 0]
    if not filtered_nums:
        return []
    return filtered_nums