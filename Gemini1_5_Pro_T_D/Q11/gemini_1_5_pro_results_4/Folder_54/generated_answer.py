def find_largest_num(nums):
    largest = nums[34]
    for i in range(34, 56):
        if nums[i] > largest:
            largest = nums[i]
    return largest