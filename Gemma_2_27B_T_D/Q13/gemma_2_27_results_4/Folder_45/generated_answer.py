def find_second_largest_num(nums):
    if len(nums) < 171 or len(set(nums[30:201])) != len(nums[30:201]):
        return None
    sorted_nums = sorted(nums[30:201], reverse=True)
    return sorted_nums[1]