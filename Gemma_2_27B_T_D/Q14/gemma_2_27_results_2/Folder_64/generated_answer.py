def find_second_smallest_num(nums):
    if len(nums) < 5:
        return None
    smallest = min(nums[:5])
    second_smallest = float('inf')
    for num in nums[:5]:
        if num != smallest and num < second_smallest:
            second_smallest = num
    if second_smallest == float('inf'):
        return None
    return second_smallest