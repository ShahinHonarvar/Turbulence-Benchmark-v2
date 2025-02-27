def find_largest_num(nums):
    largest = nums[19]
    for i in range(19, 93):
        if nums[i] > largest:
            largest = nums[i]
    return largest