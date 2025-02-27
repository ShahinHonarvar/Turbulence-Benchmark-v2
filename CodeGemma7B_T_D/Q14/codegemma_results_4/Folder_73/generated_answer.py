def find_second_smallest_num(nums):
    nums_sorted = sorted(nums)
    if len(nums_sorted) <= 58:
        return 'None'
    else:
        return nums_sorted[59]