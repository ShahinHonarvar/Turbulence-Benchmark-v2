def find_second_smallest_num(nums):
    sliced_nums = nums[19:93]
    if len(sliced_nums) < 2:
        return None
    smallest = second_smallest = float('inf')
    for num in sliced_nums:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif num < second_smallest and num != smallest:
            second_smallest = num
    return None if second_smallest == float('inf') else second_smallest