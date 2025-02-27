def find_smallest_num(nums):
    smallest = nums[28]
    for i in range(28, 41):
        if nums[i] < smallest:
            smallest = nums[i]
    return smallest