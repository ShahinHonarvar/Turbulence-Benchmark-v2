def find_second_smallest_num(nums):
    sublist = nums[246:751]
    if len(sublist) < 2:
        return None
    smallest = float('inf')
    second_smallest = float('inf')
    for num in sublist:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif num < second_smallest and num != smallest:
            second_smallest = num
    return second_smallest if second_smallest != float('inf') else None