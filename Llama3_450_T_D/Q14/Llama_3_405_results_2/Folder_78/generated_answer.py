def find_second_smallest_num(nums):
    if len(nums) < 79:
        return None
    nums_slice = nums[17:79]
    if len(nums_slice) < 2:
        return None
    nums_set = set(nums_slice)
    if len(nums_set) < 2:
        return None
    return sorted(nums_set)[1]