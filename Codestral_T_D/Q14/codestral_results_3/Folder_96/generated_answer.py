def find_second_smallest_num(nums):
    if 50 <= len(nums) <= 200:
        sublist = nums[50:201]
        sublist.sort()
        if len(sublist) > 1:
            return sublist[1]
    return None