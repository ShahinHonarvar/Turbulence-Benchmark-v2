def find_second_smallest_num(nums):
    if len(nums) < 605 - 533 + 1:
        return None
    sublist = nums[533:606]
    smallest = min(sublist)
    second_smallest = max(sublist)
    for num in sublist:
        if num != smallest and num < second_smallest:
            second_smallest = num
    return second_smallest