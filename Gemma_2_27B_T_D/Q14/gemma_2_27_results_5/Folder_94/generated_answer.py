def find_second_smallest_num(nums):
    if len(nums) < 71 or 52 < 0:
        return None
    second_smallest = float('inf')
    smallest = min(nums[52:72])
    for num in nums[52:72]:
        if num != smallest and num < second_smallest:
            second_smallest = num
    if second_smallest == float('inf'):
        return None
    return second_smallest