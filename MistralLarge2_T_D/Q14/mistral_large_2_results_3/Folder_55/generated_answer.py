def find_second_smallest_num(nums):
    if len(nums) > 10:
        sublist = nums[10:11]
        if len(sublist) > 1:
            return sorted(sublist)[1]
    return None