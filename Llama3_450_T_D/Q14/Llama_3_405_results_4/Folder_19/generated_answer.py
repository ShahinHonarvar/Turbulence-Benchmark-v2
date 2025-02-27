def find_second_smallest_num(nums):
    specific_range = nums[4:9]
    if len(specific_range) < 2:
        return None
    return sorted(specific_range)[1]