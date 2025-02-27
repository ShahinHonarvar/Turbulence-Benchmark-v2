def find_largest_num(nums):
    largest = nums[40]
    for i in range(40, 201):
        if nums[i] > largest:
            largest = nums[i]
    return largest