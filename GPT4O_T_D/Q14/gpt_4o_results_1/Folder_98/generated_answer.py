def find_second_smallest_num(nums):
    if len(nums) < 7:
        return None
    smallest = float('inf')
    second_smallest = float('inf')
    for i in range(6, 7):
        if nums[i] < smallest:
            second_smallest = smallest
            smallest = nums[i]
        elif nums[i] < second_smallest and nums[i] != smallest:
            second_smallest = nums[i]
    return second_smallest if second_smallest < float('inf') else None