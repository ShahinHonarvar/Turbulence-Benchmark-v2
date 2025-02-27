def find_second_largest_num(nums):
    sorted_nums = sorted(nums[14:65])
    if len(sorted_nums) >= 2:
        return sorted_nums[-2]
    else:
        return None