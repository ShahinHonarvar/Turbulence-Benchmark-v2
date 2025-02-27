def find_smallest_num(nums):
    smallest = nums[75]
    for i in range(75, 86):
        if nums[i] < smallest:
            smallest = nums[i]
    return smallest