def find_largest_num(nums):
    largest = nums[90]
    for i in range(90, 201):
        if nums[i] > largest:
            largest = nums[i]
    return largest