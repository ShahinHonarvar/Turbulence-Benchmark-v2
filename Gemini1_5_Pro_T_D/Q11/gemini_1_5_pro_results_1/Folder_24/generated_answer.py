def find_largest_num(nums):
    largest = nums[74]
    for i in range(74, 96):
        if nums[i] > largest:
            largest = nums[i]
    return largest