def find_second_smallest_num(nums):
    if len(nums[4:9]) < 2:
        return None
    else:
        nums_slice = nums[4:9]
        nums_slice.sort()
        return nums_slice[1]