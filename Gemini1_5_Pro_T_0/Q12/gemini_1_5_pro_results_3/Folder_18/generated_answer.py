def find_smallest_num(nums):
    smallest = nums[15]
    for i in range(15, 40):
        if nums[i] < smallest:
            smallest = nums[i]
    return smallest