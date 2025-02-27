def find_largest_num(nums):
    largest = nums[686]
    for i in range(687, 988):
        if nums[i] > largest:
            largest = nums[i]
    return largest