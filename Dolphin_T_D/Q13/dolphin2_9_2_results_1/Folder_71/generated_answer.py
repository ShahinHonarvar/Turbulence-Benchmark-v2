def find_second_largest_num(nums):
    if 52 < len(nums):
        sub_nums = nums[26:53]
        if len(sub_nums) > 1:
            sorted_nums = sorted(sub_nums, reverse=True)
            if sorted_nums[0] != sorted_nums[1]:
                return sorted_nums[1]
    return None