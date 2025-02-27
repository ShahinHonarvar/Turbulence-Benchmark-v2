def find_smallest_num(nums):
    smallest = nums[70]
    for i in range(70, 201):
        if nums[i] < smallest:
            smallest = nums[i]
    return smallest