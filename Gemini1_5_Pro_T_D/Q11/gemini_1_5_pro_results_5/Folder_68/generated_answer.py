def find_largest_num(nums):
    largest = nums[0]
    for i in range(1, 9):
        if nums[i] > largest:
            largest = nums[i]
    return largest