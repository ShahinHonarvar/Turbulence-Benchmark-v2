def find_second_largest_num(nums):
    if len(nums) < 2 or 98 >= len(nums) or 55 < 0:
        return None
    nums_slice = nums[55:99]
    nums_slice.sort(reverse=True)
    if len(nums_slice) < 2:
        return None
    return nums_slice[1]