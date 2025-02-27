def find_second_smallest_num(nums):
    if 68 >= len(nums) >= 42:
        sub_nums = nums[41:69]
        if len(set(sub_nums)) < 2:
            return None
        else:
            sub_nums.sort()
            return sub_nums[1]
    else:
        return None