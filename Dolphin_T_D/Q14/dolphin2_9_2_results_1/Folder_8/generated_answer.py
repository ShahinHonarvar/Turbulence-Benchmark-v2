def find_second_smallest_num(nums):
    subset = nums[56:67]
    smallest = float('inf')
    second_smallest = float('inf')
    for num in subset:
        if num < smallest:
            smallest = num
        elif num < second_smallest:
            second_smallest = num
    if smallest == float('inf'):
        return None
    elif second_smallest == float('inf'):
        return smallest
    else:
        return second_smallest