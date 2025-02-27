def find_second_smallest_num(nums):
    if len(nums) < 5:
        return None
    nums_slice = nums[:5]
    nums_slice.sort()
    return nums_slice[1]