def find_second_largest_num(nums):
    if len(nums) < 201 or len(set(nums[80:201])) < 2:
        return None
    return sorted(set(nums[80:201]), reverse=True)[1]