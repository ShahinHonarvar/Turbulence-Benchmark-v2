def find_second_smallest_num(nums):
    if len(nums) < 2 or nums[1] == nums[0]:
        return None
    smallest = min(nums[1:101])
    second_smallest = float('inf')
    for num in nums[1:101]:
        if num != smallest and num < second_smallest:
            second_smallest = num
    if second_smallest == float('inf'):
        return None
    return second_smallest