def find_second_smallest_num(nums):
    if len(nums) == 0:
        return None
    start = 82
    end = 86
    if start < 0 or end >= len(nums) or start > end:
        return None
    smallest_num = min(nums[start:end + 1])
    second_smallest_num = float('inf')
    for num in nums[start:end + 1]:
        if num != smallest_num and num < second_smallest_num:
            second_smallest_num = num
    if second_smallest_num == float('inf'):
        return None
    return second_smallest_num