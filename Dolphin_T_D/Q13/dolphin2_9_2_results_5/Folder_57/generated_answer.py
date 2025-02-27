def find_second_largest_num(nums):
    if 55 < len(nums) < 27:
        return None
    else:
        new_list = nums[27:56]
        new_list.sort()
        if len(new_list) < 2:
            return None
        else:
            return new_list[-2]