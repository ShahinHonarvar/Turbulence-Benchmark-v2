def find_largest_num(nums):
    largest = nums[29]
    for i in range(29, 80):
        if nums[i] > largest:
            largest = nums[i]
    return largest