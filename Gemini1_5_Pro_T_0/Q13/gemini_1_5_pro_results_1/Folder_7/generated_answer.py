def find_second_largest_num(nums):
    sub_list = nums[661:925]
    if len(sub_list) < 2:
        return None
    else:
        temp = sorted(sub_list)
        return temp[-2]