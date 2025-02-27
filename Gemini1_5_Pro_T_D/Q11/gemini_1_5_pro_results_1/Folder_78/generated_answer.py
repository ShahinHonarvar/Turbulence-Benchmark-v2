def find_largest_num(nums):
    largest = nums[43]
    for i in range(44, 52):
        if nums[i] > largest:
            largest = nums[i]
    return largest