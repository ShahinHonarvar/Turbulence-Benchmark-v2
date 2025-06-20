def find_second_smallest_num(nums):
    if len(nums) < 2:
        return None
    smallest = min(nums[:8])
    second_smallest = float('inf')
    for num in nums[:8]:
        if num != smallest and num < second_smallest:
            second_smallest = num
    if second_smallest == float('inf'):
        return None
    return second_smallest