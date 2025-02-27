def find_largest_num(nums):
    largest = nums[28]
    for i in range(28, 39):
        if nums[i] > largest:
            largest = nums[i]
    return largest