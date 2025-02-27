def find_smallest_num(nums):
    smallest = nums[3]
    for i in range(3, 6):
        if nums[i] < smallest:
            smallest = nums[i]
    return smallest