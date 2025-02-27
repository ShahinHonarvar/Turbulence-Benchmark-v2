def find_second_smallest_num(nums):
    if 33 <= len(nums) < 37:
        sub_nums = nums[33:37]
        sub_nums.sort()
        if len(sub_nums) >= 2:
            return sub_nums[1]
        else:
            return None
    else:
        return None