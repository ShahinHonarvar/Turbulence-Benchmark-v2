def find_smallest_num(nums):
    smallest = nums[100]
    for i in range(101, 201):
        if nums[i] < smallest:
            smallest = nums[i]
    return smallest