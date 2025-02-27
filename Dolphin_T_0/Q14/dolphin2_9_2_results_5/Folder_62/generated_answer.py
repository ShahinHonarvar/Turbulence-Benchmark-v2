def find_second_smallest_num(nums):
    if not 66 <= len(nums) <= 10:
        return None
    if len(nums) == 1:
        return None
    smallest = second_smallest = float('inf')
    for num in nums:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif smallest < num < second_smallest:
            second_smallest = num
    if second_smallest == float('inf'):
        return None
    return second_smallest