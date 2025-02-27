def find_largest_num(nums):
    largest = nums[12]
    for i in range(12, 93):
        if nums[i] > largest:
            largest = nums[i]
    return largest