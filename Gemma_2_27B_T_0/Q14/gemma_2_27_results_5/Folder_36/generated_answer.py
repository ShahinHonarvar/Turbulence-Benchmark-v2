def find_second_smallest_num(nums):
    if len(nums) < 556 - 209 + 1:
        return None
    sub_list = nums[209:557]
    sub_list.sort()
    if len(sub_list) < 2:
        return None
    return sub_list[1]