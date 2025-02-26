def find_second_smallest_num(nums):
    if len(nums) <= 22:
        return None
    subset = nums[22:51]
    if len(subset) < 2:
        return None
    smallest = float('inf')
    second_smallest = float('inf')
    for num in subset:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif num < second_smallest and num != smallest:
            second_smallest = num
    return second_smallest if second_smallest != float('inf') else None