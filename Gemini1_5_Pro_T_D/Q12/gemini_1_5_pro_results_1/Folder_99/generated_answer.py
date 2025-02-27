def find_smallest_num(nums):
    smallest = nums[409]
    for i in range(409, 743):
        if nums[i] < smallest:
            smallest = nums[i]
    return smallest