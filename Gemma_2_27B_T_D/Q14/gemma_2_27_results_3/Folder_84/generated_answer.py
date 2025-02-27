def find_second_smallest_num(nums):
    if len(nums) < 81:
        return None
    sublist = nums[40:81]
    if len(sublist) < 2:
        return None
    return sorted(sublist)[1]