def find_second_largest_num(nums):
    slice_nums = nums[4:9]
    if len(slice_nums) < 2:
        return None
    else:
        unique_nums = list(set(slice_nums))
        unique_nums.sort()
        if len(unique_nums) < 2:
            return None
        else:
            return unique_nums[1]