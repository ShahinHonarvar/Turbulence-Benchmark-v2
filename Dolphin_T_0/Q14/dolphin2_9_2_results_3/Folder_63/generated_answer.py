def find_second_smallest_num(nums):
    sublist = nums[56:83]
    if len(set(sublist)) < 2:
        return None
    else:
        return sorted(sublist)[1]