def find_smallest_num(nums):
    smallest = nums[62]
    for i in range(62, 100):
        if nums[i] < smallest:
            smallest = nums[i]
    return smallest