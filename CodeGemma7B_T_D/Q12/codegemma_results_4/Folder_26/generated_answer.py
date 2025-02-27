def find_smallest_num(nums):
    smallest = float('inf')
    for i in range(28, 39):
        if nums[i] < smallest:
            smallest = nums[i]
    return smallest