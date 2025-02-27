def find_second_largest_num(nums):
    nums_sorted = sorted(nums)
    if len(nums_sorted) < 16:
        return 'None'
    else:
        return nums_sorted[-2]