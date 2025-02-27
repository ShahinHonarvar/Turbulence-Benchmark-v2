def find_second_largest_num(nums):
    if len(nums) < 201 or len(nums) < 81:
        return None
    nums_slice = nums[80:201]
    if len(nums_slice) < 2:
        return None
    nums_slice.sort(reverse=True)
    if len(nums_slice) < 2:
        return None
    return nums_slice[1]