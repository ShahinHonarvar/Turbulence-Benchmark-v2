def find_second_smallest_num(nums):
    if len(nums[3:6]) >= 2:
        return sorted(nums[3:6])[1]
    else:
        return None