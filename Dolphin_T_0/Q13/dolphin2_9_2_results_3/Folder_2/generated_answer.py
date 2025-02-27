def find_second_largest_num(nums):
    if 15 <= len(nums) <= 39:
        nums_slice = nums[15:40]
        max_nums = max(nums_slice)
        nums_slice.remove(max_nums)
        if len(nums_slice) > 0:
            return max(nums_slice)
    return None