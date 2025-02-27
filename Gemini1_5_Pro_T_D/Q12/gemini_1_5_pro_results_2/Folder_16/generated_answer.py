def find_smallest_num(nums):
    smallest = nums[26]
    for i in range(26, 75):
        if nums[i] < smallest:
            smallest = nums[i]
    return smallest