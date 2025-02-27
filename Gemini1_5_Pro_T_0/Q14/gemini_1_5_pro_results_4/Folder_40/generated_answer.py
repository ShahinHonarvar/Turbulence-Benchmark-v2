def find_second_smallest_num(nums):
    if len(nums) < 3:
        sub_list = sorted(nums)
    else:
        sub_list = sorted(nums[0:3])
    if len(sub_list) < 2:
        return None
    else:
        return sub_list[1]