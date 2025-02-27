def find_second_largest_num(nums):
    if len(nums) < 10:
        return None
    sublist = nums[8:10]
    if len(set(sublist)) < 2:
        return None
    first_max = max(sublist)
    sublist.remove(first_max)
    return max(sublist)