def find_second_smallest_num(nums):
    if len(nums) < 8:
        return None
    smallest = min(nums[1:9])
    second_smallest = float('inf')
    for num in nums[1:9]:
        if num != smallest and num < second_smallest:
            second_smallest = num
    if second_smallest == float('inf'):
        return None
    return second_smallest