def find_largest_num(nums):
    largest = nums[22]
    for i in range(22, 89):
        if nums[i] > largest:
            largest = nums[i]
    return largest