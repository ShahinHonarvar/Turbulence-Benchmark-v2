def find_second_smallest_num(nums):
    sub_list = nums[527:539]
    if len(sub_list) >= 2:
        sub_list.sort()
        return sub_list[1]
    else:
        return None