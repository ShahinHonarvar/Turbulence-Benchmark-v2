def find_smallest_num(nums):
    smallest = nums[0]
    for i in range(1, 6):
        if nums[i] < smallest:
            smallest = nums[i]
    return smallest