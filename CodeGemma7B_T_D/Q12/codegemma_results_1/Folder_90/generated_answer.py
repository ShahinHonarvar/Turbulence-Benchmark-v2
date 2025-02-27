def find_smallest_num(nums):
    smallest = float('inf')
    for i in range(639, 976):
        if nums[i] < smallest:
            smallest = nums[i]
    return smallest