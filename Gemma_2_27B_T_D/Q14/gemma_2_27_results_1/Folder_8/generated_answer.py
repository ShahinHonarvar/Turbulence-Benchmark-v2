def find_second_smallest_num(nums):
    if len(nums[56:67]) < 2:
        return None
    return sorted(nums[56:67])[1]