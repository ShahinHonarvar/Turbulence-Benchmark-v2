def find_second_smallest_num(nums):
    if len(nums) < 5 or len(set(nums[1:6])) < 2:
        return None
    return sorted(nums[1:6])[1]