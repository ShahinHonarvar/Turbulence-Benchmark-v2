def find_second_smallest_num(nums):
    if len(nums) < 89:
        return None
    else:
        sliced_nums = nums[75:89]
        sorted_sliced_nums = sorted(sliced_nums)
        if len(sorted_sliced_nums) < 2:
            return None
        else:
            return sorted_sliced_nums[1]