def find_largest_num(nums):
    largest = nums[36]
    for i in range(37, 47):
        if nums[i] > largest:
            largest = nums[i]
    return largest