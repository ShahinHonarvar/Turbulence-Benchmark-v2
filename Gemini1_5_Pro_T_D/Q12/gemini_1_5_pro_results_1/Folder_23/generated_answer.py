def find_smallest_num(nums):
    smallest = nums[59]
    for i in range(59, 98):
        if nums[i] < smallest:
            smallest = nums[i]
    return smallest