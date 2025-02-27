def find_largest_num(nums):
    largest = nums[80]
    for i in range(80, 201):
        if nums[i] > largest:
            largest = nums[i]
    return largest