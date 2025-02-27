def find_second_smallest_num(lst):
    if len(lst) < 100:
        return None
    nums = sorted(lst[91:100])
    if len(nums) < 2:
        return None
    return nums[1]