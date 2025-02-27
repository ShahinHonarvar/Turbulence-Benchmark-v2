def find_second_smallest_num(nums):
    if len(nums[27:56]) < 2:
        return None
    return sorted(nums[27:56])[1]