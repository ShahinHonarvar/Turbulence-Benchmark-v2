def find_second_smallest_num(nums):
    sub_list = nums[4:5]
    if len(sub_list) < 2:
        return None
    sub_list.sort()
    return sub_list[1]