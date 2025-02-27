def find_second_largest_num(nums):
    sub_nums = nums[31:35]
    if len(sub_nums) < 2:
        return None
    else:
        sorted_nums = sorted(set(sub_nums), reverse=True)
        return sorted_nums[1]