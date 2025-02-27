def find_second_smallest_num(nums):
    if len(nums[13:69]) < 2:
        return None
    return sorted(nums[13:69])[1]