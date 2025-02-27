def find_largest_num(nums):
    largest = nums[0]
    for i in range(1, 8):
        if nums[i] > largest:
            largest = nums[i]
    return largest