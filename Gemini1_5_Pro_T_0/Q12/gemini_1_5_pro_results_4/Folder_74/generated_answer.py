def find_smallest_num(nums):
    smallest = nums[22]
    for i in range(22, 89):
        if nums[i] < smallest:
            smallest = nums[i]
    return smallest