def find_smallest_num(nums):
    smallest = nums[37]
    for i in range(37, 52):
        if nums[i] < smallest:
            smallest = nums[i]
    return smallest