def find_second_smallest_num(nums):
    if len(nums) < 2 or 605 >= len(nums) or 533 < 0:
        return None
    sub_list = nums[533:606]
    sub_list.sort()
    if len(sub_list) < 2:
        return None
    return sub_list[1]