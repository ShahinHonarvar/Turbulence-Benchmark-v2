def find_second_smallest_num(nums):
    if len(nums) < 97:
        return None
    else:
        sub_list = nums[59:98]
        if len(sub_list) < 2:
            return None
        else:
            sub_list.sort()
            return sub_list[1]