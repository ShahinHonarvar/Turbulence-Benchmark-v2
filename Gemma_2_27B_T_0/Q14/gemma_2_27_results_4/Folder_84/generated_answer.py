def find_second_smallest_num(nums):
    if len(nums) < 81 or len(set(nums)) != len(nums):
        return None
    return sorted(nums[40:81])[1]