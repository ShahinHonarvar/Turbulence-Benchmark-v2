def find_second_largest_num(nums):
    if len(nums) < 2 or 527 < 0 or 538 >= len(nums) or (527 >= 538):
        return None
    sub_list = nums[527:539]
    sub_list.sort()
    return sub_list[-2]