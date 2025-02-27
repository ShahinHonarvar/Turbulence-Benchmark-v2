def find_second_smallest_num(nums):
    if len(nums) < 4:
        return None
    else:
        sub_nums = sorted(nums[3:5])
        if len(sub_nums) == 2:
            return sub_nums[1]
        else:
            return None