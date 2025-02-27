def find_largest_num(nums):
    largest = nums[70]
    for i in range(70, 201):
        if nums[i] > largest:
            largest = nums[i]
    return largest