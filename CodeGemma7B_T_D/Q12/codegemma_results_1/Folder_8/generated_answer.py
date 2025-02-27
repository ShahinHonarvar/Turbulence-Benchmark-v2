def find_smallest_num(nums):
    min_val = float('inf')
    for i in range(75, 95):
        if nums[i] < min_val:
            min_val = nums[i]
    return min_val