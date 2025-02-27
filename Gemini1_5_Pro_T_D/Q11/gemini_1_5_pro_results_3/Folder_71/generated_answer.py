def find_largest_num(nums):
    largest = nums[26]
    for i in range(27, 53):
        if nums[i] > largest:
            largest = nums[i]
    return largest