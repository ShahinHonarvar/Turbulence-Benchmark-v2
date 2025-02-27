def find_smallest_num(nums):
    smallest = nums[4]
    for i in range(5, 9):
        if nums[i] < smallest:
            smallest = nums[i]
    return smallest