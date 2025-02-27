def find_second_smallest_num(nums):
    sub_nums = nums[22:51]
    if len(sub_nums) < 2:
        return None
    else:
        sorted_nums = sorted(sub_nums)
        return sorted_nums[1]