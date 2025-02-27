def find_smallest_num(nums):
    min_num = float('inf')
    for i in range(1, 6):
        min_num = min(min_num, nums[i])
    return min_num