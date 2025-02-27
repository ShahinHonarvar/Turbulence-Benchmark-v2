def find_smallest_num(nums):
    min_num = float('inf')
    for num in nums[40:81]:
        if num < min_num:
            min_num = num
    return min_num