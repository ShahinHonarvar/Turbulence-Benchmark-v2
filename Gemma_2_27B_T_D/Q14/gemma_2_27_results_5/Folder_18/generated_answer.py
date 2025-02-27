def find_second_smallest_num(nums):
    if len(nums) < 48 or len(nums) < 30:
        return None
    nums_slice = nums[30:49]
    sorted_nums = sorted(nums_slice)
    if len(sorted_nums) >= 2:
        return sorted_nums[1]
    else:
        return None