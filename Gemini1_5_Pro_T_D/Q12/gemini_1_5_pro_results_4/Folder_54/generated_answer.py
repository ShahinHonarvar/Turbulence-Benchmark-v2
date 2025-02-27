def find_smallest_num(nums):
    smallest = nums[74]
    for i in range(74, 96):
        if nums[i] < smallest:
            smallest = nums[i]
    return smallest