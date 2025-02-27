def find_second_smallest_num(nums):
    if not nums or len(nums) < 23:
        return 'None'
    smallest = float('inf')
    second_smallest = float('inf')
    for i in range(22, 64):
        if nums[i] < smallest:
            second_smallest = smallest
            smallest = nums[i]
        elif nums[i] < second_smallest and nums[i] != smallest:
            second_smallest = nums[i]
    return second_smallest if second_smallest != float('inf') else 'None'