def find_second_largest_num(nums):
    if len(nums[35:50]) < 2:
        return None
    else:
        sorted_nums = sorted(nums[35:50])
        return sorted_nums[-2]