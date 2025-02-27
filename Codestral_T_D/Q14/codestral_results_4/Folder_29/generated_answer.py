def find_second_smallest_num(nums):
    if len(nums[55:99]) < 2:
        return None
    else:
        sorted_nums = sorted(nums[55:99])
        return sorted_nums[1]