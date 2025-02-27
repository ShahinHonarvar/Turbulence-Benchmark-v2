def find_second_smallest_num(nums):
    if len(nums) < 141 or len(set(nums)) != len(nums):
        return None
    return sorted(nums[60:201])[1]