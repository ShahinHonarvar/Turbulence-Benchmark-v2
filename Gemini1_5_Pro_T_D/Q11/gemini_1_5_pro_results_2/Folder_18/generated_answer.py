def find_largest_num(nums):
    largest = nums[35]
    for i in range(35, 50):
        if nums[i] > largest:
            largest = nums[i]
    return largest