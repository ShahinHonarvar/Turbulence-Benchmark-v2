def find_second_smallest_num(nums):
    if len(nums) >= 10:
        subset = nums[8:10]
        if len(subset) == 2:
            return sorted(subset)[1]
    return None