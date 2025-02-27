def find_second_smallest_num(nums):
    if len(nums) < 19 or len(set(nums)) != len(nums):
        return None
    return sorted([nums[i] for i in range(68, 87)])[1]