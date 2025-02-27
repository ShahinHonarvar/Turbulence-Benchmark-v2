def find_second_largest_num(nums):
    if len(nums) < 200:
        return None
    else:
        sub_list = nums[100:201]
        max_num = max(sub_list)
        sub_list.remove(max_num)
        if len(sub_list) == 0:
            return None
        else:
            return max(sub_list)