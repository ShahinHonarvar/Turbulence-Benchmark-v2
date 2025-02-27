def find_second_largest_num(nums):
    if len(nums) <= 100:
        sub_list = nums[10:101]
    else:
        sub_list = nums[10:100]
    if len(sub_list) < 2:
        return None
    sub_list.sort(reverse=True)
    return sub_list[1]