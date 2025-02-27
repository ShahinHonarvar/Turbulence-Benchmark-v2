def find_second_smallest_num(nums):
    if len(nums) < 78 - 17 + 1 or len(set(nums)) < 2:
        return None
    return sorted(nums[17:79])[1]