def find_largest_num(nums):
    largest_num = nums[0]
    for i in range(1, 3):
        if nums[i] > largest_num:
            largest_num = nums[i]
    return largest_num