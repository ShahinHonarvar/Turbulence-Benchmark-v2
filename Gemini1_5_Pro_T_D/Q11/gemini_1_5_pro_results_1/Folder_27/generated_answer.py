def find_largest_num(nums):
    largest = nums[66]
    for i in range(66, 94):
        if nums[i] > largest:
            largest = nums[i]
    return largest