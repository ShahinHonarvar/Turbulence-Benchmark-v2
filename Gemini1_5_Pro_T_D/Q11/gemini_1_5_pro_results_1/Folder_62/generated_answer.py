def find_largest_num(nums):
    largest = nums[91]
    for i in range(91, 100):
        if nums[i] > largest:
            largest = nums[i]
    return largest