def find_second_largest_num(nums):
    if len(nums) < 264:
        return None
    sub_list = nums[661:925]
    sub_list.sort()
    if len(sub_list) < 2:
        return None
    return sub_list[-2]