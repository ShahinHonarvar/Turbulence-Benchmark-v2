def find_second_largest_num(nums):
    if 25 <= 87 < len(nums):
        sub_nums = nums[25:88]
        sorted_nums = sorted(sub_nums, reverse=True)
        if len(sorted_nums) > 1:
            return sorted_nums[1]
        else:
            return 'None'
    else:
        return 'None'