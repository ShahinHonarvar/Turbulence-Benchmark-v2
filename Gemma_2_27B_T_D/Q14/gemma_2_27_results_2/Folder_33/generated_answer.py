def find_second_smallest_num(nums):
    if len(nums[262:747]) < 2:
        return None
    return sorted(nums[262:747])[1]