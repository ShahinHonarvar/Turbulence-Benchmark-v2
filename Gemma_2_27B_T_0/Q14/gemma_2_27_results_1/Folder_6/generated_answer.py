def find_second_smallest_num(nums):
    if len(nums) < 51 or len(set(nums)) != len(nums):
        return None
    return sorted(nums[29:80])[1]