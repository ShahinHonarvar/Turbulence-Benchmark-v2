def find_largest_num(nums):
    largest = nums[661]
    for i in range(661, 925):
        if nums[i] > largest:
            largest = nums[i]
    return largest