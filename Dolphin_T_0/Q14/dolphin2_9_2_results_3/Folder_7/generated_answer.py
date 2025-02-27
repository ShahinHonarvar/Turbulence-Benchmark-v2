def find_second_smallest_num(nums):
    if len(nums) < 2:
        return None
    second_smallest = float('inf')
    smallest = float('inf')
    for i in range(686, 988):
        if nums[i] < smallest:
            second_smallest = smallest
            smallest = nums[i]
        elif nums[i] < second_smallest:
            second_smallest = nums[i]
    if second_smallest == float('inf'):
        return None
    return second_smallest