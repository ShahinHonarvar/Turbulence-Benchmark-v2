def find_smallest_num(nums):
    smallest = nums[36]
    for i in range(36, 47):
        if nums[i] < smallest:
            smallest = nums[i]
    return smallest