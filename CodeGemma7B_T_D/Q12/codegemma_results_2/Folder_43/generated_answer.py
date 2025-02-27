def find_smallest_num(nums):
    min_num = float('inf')
    for i in range(23, 24):
        if nums[i] < min_num:
            min_num = nums[i]
    return min_num