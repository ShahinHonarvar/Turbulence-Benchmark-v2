def find_second_smallest_num(nums):
    if len(nums) < 60:
        return None
    else:
        sub_nums = nums[25:60]
        sorted_sub_nums = sorted(sub_nums)
        return sorted_sub_nums[1]