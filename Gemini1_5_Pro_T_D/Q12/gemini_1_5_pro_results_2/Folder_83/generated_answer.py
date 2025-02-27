def find_smallest_num(nums):
    smallest = nums[90]
    for i in range(90, 201):
        if nums[i] < smallest:
            smallest = nums[i]
    return smallest