def find_smallest_num(nums):
    smallest = nums[19]
    for i in range(19, 93):
        if nums[i] < smallest:
            smallest = nums[i]
    return smallest