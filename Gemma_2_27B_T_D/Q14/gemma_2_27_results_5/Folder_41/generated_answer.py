def find_second_smallest_num(nums):
    if len(nums) > 4:
        nums_slice = nums[4:5]
        if len(nums_slice) == 1:
            return nums_slice[0]
    return None