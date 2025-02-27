def find_smallest_num(nums):
    smallest = nums[20]
    for i in range(20, 31):
        if nums[i] < smallest:
            smallest = nums[i]
    return smallest