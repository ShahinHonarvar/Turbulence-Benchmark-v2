def find_second_smallest_num(nums):
    subset = nums[4:9]
    if len(subset) < 2:
        return None
    first_smallest = float('inf')
    second_smallest = float('inf')
    for num in subset:
        if num < first_smallest:
            second_smallest = first_smallest
            first_smallest = num
        elif first_smallest < num < second_smallest:
            second_smallest = num
    if second_smallest == float('inf'):
        return None
    return second_smallest