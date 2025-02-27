def find_smallest_num(nums):
    smallest = nums[35]
    for i in range(35, 50):
        if nums[i] < smallest:
            smallest = nums[i]
    return smallest