def find_second_smallest_num(nums):
    sublist = nums[30:88]
    if len(sublist) < 2:
        return None
    first_smallest = float('inf')
    second_smallest = float('inf')
    for num in sublist:
        if num < first_smallest:
            second_smallest = first_smallest
            first_smallest = num
        elif num < second_smallest:
            second_smallest = num
    if second_smallest == float('inf'):
        return None
    return second_smallest