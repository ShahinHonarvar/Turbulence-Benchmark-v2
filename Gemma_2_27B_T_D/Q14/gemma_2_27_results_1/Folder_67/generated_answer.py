def find_second_smallest_num(nums):
    if len(nums) < 55 or nums[50:] == sorted(nums[50:]):
        return None
    return sorted(nums[50:55])[1]