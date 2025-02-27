def find_largest_num(nums):
    largest = nums[27]
    for i in range(27, 56):
        if nums[i] > largest:
            largest = nums[i]
    return largest