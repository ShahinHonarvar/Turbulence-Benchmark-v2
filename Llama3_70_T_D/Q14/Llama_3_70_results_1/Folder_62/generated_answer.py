def find_second_smallest_num(nums):
    second_smallest = None
    smallest = float('inf')
    for i in range(10, 67):
        if nums[i] < smallest:
            second_smallest = smallest
            smallest = nums[i]
        elif nums[i] < second_smallest and nums[i] != smallest:
            second_smallest = nums[i]
    return second_smallest