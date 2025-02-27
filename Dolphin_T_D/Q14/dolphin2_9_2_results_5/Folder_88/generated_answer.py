def find_second_smallest_num(nums):
    sub_nums = nums[5:9]
    if len(sub_nums) == 0:
        return None
    elif len(sub_nums) == 1:
        return None
    elif len(sub_nums) == 2:
        return min(sub_nums[1:])
    else:
        min_num = min(sub_nums[0:2])
        sub_nums.remove(min_num)
        return min(sub_nums)