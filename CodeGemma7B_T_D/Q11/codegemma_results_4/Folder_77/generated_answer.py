def find_largest_num(nums):
    largest = float('-inf')
    for i in range(527, 539):
        if nums[i] > largest:
            largest = nums[i]
    return largest