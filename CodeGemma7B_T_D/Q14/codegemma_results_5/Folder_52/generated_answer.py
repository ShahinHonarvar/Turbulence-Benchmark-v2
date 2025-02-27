from functools import cmp_to_key

def find_second_smallest_num(nums):
    nums_sorted = sorted(nums[64:67], key=cmp_to_key)
    if len(nums_sorted) > 1:
        return nums_sorted[1]
    return 'None'