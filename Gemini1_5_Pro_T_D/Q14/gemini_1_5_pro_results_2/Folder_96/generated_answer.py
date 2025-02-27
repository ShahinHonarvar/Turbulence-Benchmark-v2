def find_second_smallest_num(nums):
    if len(nums) < 201:
        return None
    else:
        sub_nums = nums[50:201]
        sorted_sub_nums = sorted(sub_nums)
        if len(sorted_sub_nums) >= 2:
            return sorted_sub_nums[1]
        else:
            return None