def find_second_smallest_num(nums):
    if len(nums) >= 10:
        nums_slice = nums[8:10]
        sorted_nums = sorted(nums_slice)
        if len(sorted_nums) > 1:
            return sorted_nums[1]
    return None