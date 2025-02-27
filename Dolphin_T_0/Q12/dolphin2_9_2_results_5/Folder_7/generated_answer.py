def find_smallest_num(nums):
    smallest = nums[533]
    for i in range(534, 606):
        if nums[i] < smallest:
            smallest = nums[i]
    return smallest