def find_second_largest_num(nums):
    if len(nums) < 12 or 527 < 0 or 538 >= len(nums):
        return None
    sub_list = nums[527:539]
    sub_list.sort()
    if len(sub_list) < 2:
        return None
    return sub_list[-2]