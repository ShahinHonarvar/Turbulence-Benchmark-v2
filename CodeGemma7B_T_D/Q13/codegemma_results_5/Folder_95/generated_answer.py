def find_second_largest_num(nums):
    nums_sorted = sorted(nums)[82:87]
    nums_sorted.sort(reverse=True)
    if len(nums_sorted) < 2:
        return None
    return nums_sorted[1]