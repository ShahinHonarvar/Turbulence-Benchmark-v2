def find_second_largest_num(nums):
    nums_slice = nums[310:371]
    if len(nums_slice) < 2:
        return None
    return sorted(nums_slice)[-2]