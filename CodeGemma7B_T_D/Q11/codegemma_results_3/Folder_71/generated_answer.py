def find_largest_num(nums):
    largest = float('-inf')
    for i in range(26, 53):
        if nums[i] > largest:
            largest = nums[i]
    return largest