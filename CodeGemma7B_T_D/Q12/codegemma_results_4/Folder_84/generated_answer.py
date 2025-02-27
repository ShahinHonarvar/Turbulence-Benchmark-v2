def find_smallest_num(nums):
    min_num = float('inf')
    for num in nums[31:35]:
        min_num = min(min_num, num)
    return min_num