def find_smallest_num(nums):
    smallest = nums[6]
    for i in range(6, 9):
        if nums[i] < smallest:
            smallest = nums[i]
    return smallest