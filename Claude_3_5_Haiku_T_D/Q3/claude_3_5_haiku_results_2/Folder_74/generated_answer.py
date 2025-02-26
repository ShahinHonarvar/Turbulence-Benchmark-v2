def all_pos_ints_inclusive(nums):
    if len(nums) <= 78:
        return []
    filtered_list = [num for num in nums[17:79] if num > 0]
    return filtered_list