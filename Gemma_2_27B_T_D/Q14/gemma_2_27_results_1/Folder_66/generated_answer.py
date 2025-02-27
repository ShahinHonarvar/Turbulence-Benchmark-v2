def find_second_smallest_num(nums):
    if len(nums[62:100]) < 2:
        return None
    return sorted(nums[62:100])[1]