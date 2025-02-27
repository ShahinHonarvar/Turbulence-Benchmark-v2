def find_second_smallest_num(nums):
    nums_sorted = sorted(nums[1:6])
    if len(nums_sorted) == 5:
        return nums_sorted[1]
    else:
        return None