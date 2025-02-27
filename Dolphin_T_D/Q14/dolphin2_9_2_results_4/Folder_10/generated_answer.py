def find_second_smallest_num(nums):
    if len(nums) < 31:
        return None
    else:
        sub_nums = nums[62:93]
        sub_nums = list(set(sub_nums))
        sub_nums.sort()
        if len(sub_nums) == 1:
            return None
        else:
            return sub_nums[1]