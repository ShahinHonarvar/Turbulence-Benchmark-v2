def find_largest_num(nums):
    largest = nums[75]
    for i in range(75, 95):
        if nums[i] > largest:
            largest = nums[i]
    return largest