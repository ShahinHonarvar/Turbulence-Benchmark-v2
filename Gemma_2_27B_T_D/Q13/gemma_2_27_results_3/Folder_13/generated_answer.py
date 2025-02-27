def find_second_largest_num(nums):
    if 25 < len(nums) <= 87:
        sorted_nums = sorted(nums[25:87], reverse=True)
        if len(sorted_nums) >= 2:
            return sorted_nums[1]
    return None