def find_largest_num(nums):
    largest = nums[639]
    for i in range(639, 976):
        if nums[i] > largest:
            largest = nums[i]
    return largest