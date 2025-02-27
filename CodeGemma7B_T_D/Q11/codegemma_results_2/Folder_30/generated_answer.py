def find_largest_num(nums):
    largest = float('-inf')
    for i in range(55, 99):
        if nums[i] > largest:
            largest = nums[i]
    return largest