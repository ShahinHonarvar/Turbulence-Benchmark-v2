def find_smallest_num(nums):
    smallest = nums[27]
    for i in range(27, 56):
        if nums[i] < smallest:
            smallest = nums[i]
    return smallest