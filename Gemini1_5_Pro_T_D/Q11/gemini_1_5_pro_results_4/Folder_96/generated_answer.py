def find_largest_num(nums):
    largest = nums[50]
    for i in range(50, 201):
        if nums[i] > largest:
            largest = nums[i]
    return largest