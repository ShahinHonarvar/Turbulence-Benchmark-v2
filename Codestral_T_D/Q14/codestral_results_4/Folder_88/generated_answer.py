def find_second_smallest_num(nums):
    if len(nums[6:9]) < 2:
        return None
    else:
        sorted_nums = sorted(nums[6:9])
        return sorted_nums[1]