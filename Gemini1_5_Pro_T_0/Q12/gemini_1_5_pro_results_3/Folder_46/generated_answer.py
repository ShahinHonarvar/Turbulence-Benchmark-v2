def find_smallest_num(nums):
    smallest = nums[91]
    for i in range(92, 100):
        if nums[i] < smallest:
            smallest = nums[i]
    return smallest