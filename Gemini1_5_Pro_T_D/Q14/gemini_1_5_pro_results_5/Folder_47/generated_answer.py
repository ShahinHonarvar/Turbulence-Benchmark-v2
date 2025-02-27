def find_second_smallest_num(nums):
    if len(nums) < 64:
        return None
    second_smallest = float('inf')
    smallest = float('inf')
    for i in range(22, 64):
        if nums[i] < smallest:
            second_smallest = smallest
            smallest = nums[i]
        elif nums[i] < second_smallest and nums[i] != smallest:
            second_smallest = nums[i]
    if second_smallest == float('inf'):
        return None
    return second_smallest