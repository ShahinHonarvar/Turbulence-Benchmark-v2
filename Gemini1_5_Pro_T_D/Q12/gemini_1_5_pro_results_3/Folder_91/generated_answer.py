def find_smallest_num(nums):
    smallest = nums[0]
    for i in range(1, 5):
        if nums[i] < smallest:
            smallest = nums[i]
    return smallest