def find_second_smallest_num(nums):
    if len(nums) < 9:
        return None
    slice = nums[8:10]
    if len(slice) < 2:
        return None
    return sorted(slice)[1]