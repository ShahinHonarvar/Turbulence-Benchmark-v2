def find_smallest_num(nums):
    smallest = nums[30]
    for i in range(30, 88):
        if nums[i] < smallest:
            smallest = nums[i]
    return smallest