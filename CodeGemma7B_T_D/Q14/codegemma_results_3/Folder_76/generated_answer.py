def find_second_smallest_num(nums):
    sorted_nums = sorted(nums[533:606])
    if len(sorted_nums) < 2:
        return None
    else:
        return sorted_nums[1]