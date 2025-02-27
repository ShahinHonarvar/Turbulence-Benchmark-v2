def find_second_smallest_num(nums):
    if len(nums) < 52:
        return None
    sublist = nums[43:52]
    if len(sublist) < 2:
        return None
    smallest = float('inf')
    second_smallest = float('inf')
    for num in sublist:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif smallest < num < second_smallest:
            second_smallest = num
    if second_smallest == float('inf'):
        return None
    return second_smallest