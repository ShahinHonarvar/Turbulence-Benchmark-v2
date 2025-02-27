def find_second_smallest_num(lst):
    if len(lst) <= 86:
        return None
    nums = lst[68:87]
    nums.sort()
    if len(nums) == 1:
        return None
    return nums[1]