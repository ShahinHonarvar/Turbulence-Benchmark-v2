def find_second_smallest_num(nums):
    if len(nums) < 99 or len(nums[56:99]) < 2:
        return None
    return sorted(nums[56:99])[1]