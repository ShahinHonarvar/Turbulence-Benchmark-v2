def find_second_smallest_num(nums):
    if len(nums) < 2:
        return None
    smallest = min(nums[0], nums[1])
    second_smallest = max(nums[0], nums[1])
    for i in range(2, 6):
        if nums[i] < smallest:
            second_smallest = smallest
            smallest = nums[i]
        elif nums[i] < second_smallest and nums[i] != smallest:
            second_smallest = nums[i]
    return second_smallest if second_smallest != smallest else None