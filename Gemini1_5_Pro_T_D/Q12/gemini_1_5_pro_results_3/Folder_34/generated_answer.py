def find_smallest_num(nums):
    smallest = nums[60]
    for i in range(60, 201):
        if nums[i] < smallest:
            smallest = nums[i]
    return smallest