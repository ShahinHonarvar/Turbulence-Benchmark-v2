def find_second_largest_num(nums):
    if len(nums) < 201:
        return None
    sublist = nums[80:201]
    if len(sublist) < 2:
        return None
    sublist.sort(reverse=True)
    return sublist[1]