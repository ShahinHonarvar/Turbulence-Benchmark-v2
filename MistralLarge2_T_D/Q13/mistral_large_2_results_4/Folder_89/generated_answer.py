def find_second_largest_num(nums):
    if len(nums) <= 82:
        sub_list = nums[56:83]
        if len(sub_list) < 2:
            return None
        sub_list.sort()
        return sub_list[-2]
    else:
        return None