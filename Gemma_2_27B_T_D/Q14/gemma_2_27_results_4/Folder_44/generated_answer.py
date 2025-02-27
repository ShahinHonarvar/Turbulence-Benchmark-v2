def find_second_smallest_num(nums):
    if len(nums[91:100]) < 2:
        return None
    return sorted(nums[91:100])[1]