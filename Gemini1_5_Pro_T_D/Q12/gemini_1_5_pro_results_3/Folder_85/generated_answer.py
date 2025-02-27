def find_smallest_num(nums):
    smallest = nums[2]
    for i in range(2, 7):
        if nums[i] < smallest:
            smallest = nums[i]
    return smallest