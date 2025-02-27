def find_smallest_num(nums):
    smallest = nums[26]
    for i in range(26, 53):
        if nums[i] < smallest:
            smallest = nums[i]
    return smallest