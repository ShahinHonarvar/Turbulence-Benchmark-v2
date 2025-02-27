def find_second_smallest_num(nums):
    if len(nums) < 10:
        return None
    else:
        specific_range = nums[8:10]
        sorted_specific_range = sorted(specific_range)
        if len(sorted_specific_range) < 2:
            return None
        else:
            return sorted_specific_range[1]