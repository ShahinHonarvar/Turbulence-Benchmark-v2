def find_largest_num(nums):
    largest = nums[262]
    for i in range(262, 747):
        if nums[i] > largest:
            largest = nums[i]
    return largest