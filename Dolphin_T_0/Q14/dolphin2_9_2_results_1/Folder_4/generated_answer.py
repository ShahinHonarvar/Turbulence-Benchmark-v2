def find_second_smallest_num(nums):
    if not isinstance(nums, list) or min(nums) < 0 or len(set(nums)) != len(nums):
        return None
    return sorted(nums)[1]