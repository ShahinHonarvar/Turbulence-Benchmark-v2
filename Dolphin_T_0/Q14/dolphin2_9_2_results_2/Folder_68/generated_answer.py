def find_second_smallest_num(nums):
    if len(nums) < 2:
        return None
    smallest = float('inf')
    second_smallest = float('inf')
    for num in nums:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif num < second_smallest:
            second_smallest = num
    if second_smallest == float('inf'):
        return None
    return second_smallest