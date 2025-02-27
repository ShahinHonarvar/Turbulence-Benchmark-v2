def find_second_smallest_num(nums):
    if len(nums) >= 9:
        nums_slice = nums[6:9]
        sorted_nums = sorted(nums_slice)
        if len(sorted_nums) >= 2:
            return sorted_nums[1]
    return None