def find_largest_num(nums):
    largest = nums[60]
    for i in range(60, 201):
        if nums[i] > largest:
            largest = nums[i]
    return largest