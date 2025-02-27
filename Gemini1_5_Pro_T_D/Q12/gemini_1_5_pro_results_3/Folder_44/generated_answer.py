def find_smallest_num(nums):
    smallest = nums[10]
    for i in range(10, 67):
        if nums[i] < smallest:
            smallest = nums[i]
    return smallest