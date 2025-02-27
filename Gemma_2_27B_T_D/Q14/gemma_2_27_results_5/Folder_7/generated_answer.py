def find_second_smallest_num(nums):
    if len(nums) < 988 or 686 < 0:
        return None
    sublist = nums[686:988]
    if len(sublist) < 2:
        return None
    smallest = min(sublist)
    second_smallest = max(sublist)
    for num in sublist:
        if num != smallest and num < second_smallest:
            second_smallest = num
    return second_smallest