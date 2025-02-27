def find_second_smallest_num(nums):
    if len(nums[6:7]) >= 2:
        sorted_nums = sorted(nums[6:7])
        return sorted_nums[1]
    else:
        return None