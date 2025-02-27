def find_second_largest_num(nums):
    if len(nums) < 2 or 538 >= len(nums) or 527 < 0:
        return None
    sliced_list = nums[527:539]
    sliced_list.sort(reverse=True)
    if len(sliced_list) < 2:
        return None
    return sliced_list[1]