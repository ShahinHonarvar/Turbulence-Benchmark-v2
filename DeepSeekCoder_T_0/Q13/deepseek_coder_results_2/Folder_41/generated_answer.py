def find_second_largest_num(nums):
    if len(nums) < 7:
        return None
    sub_list = nums[6:7]
    if len(sub_list) < 2:
        return None
    sub_list.sort(reverse=True)
    return sub_list[1]