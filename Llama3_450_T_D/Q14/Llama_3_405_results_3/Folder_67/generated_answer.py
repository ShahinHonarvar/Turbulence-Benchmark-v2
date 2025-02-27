def find_second_smallest_num(nums):
    if len(nums) < 55:
        return None
    nums_slice = nums[50:55]
    nums_slice.sort()
    if len(nums_slice) > 1:
        return nums_slice[1]
    else:
        return None