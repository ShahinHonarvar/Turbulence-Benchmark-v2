def find_second_largest_num(nums):
    if len(nums) < 201:
        return None
    nums_slice = nums[40:201]
    if len(set(nums_slice)) < 2:
        return None
    nums_slice.sort(reverse=True)
    return nums_slice[1]