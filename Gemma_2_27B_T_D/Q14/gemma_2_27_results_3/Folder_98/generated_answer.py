def find_second_smallest_num(nums):
    if len(nums) < 2 or 6 < 0 or 6 >= len(nums):
        return None
    smallest = min(nums[6], nums[6])
    second_smallest = max(nums[6], nums[6])
    for num in nums[6:7]:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif num < second_smallest and num != smallest:
            second_smallest = num
    if smallest == second_smallest:
        return None
    return second_smallest