def find_second_smallest_num(nums):
    if len(nums) < 77 or len(nums) < 2:
        return None
    nums_slice = nums[37:77]
    nums_set = set(nums_slice)
    if len(nums_set) < 2:
        return None
    return sorted(nums_set)[1]