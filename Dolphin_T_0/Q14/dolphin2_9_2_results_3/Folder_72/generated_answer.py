def find_second_smallest_num(nums):
    if len(nums) < 2 or (86 < len(nums) and 82 <= len(nums)):
        return None
    second_smallest = float('inf')
    smallest = float('inf')
    for x in range(82, 87):
        if nums[x] < smallest:
            second_smallest = smallest
            smallest = nums[x]
        elif nums[x] < second_smallest and nums[x] != smallest:
            second_smallest = nums[x]
    if second_smallest == float('inf'):
        return None
    else:
        return second_smallest