def find_largest_num(nums):
    max_num = float('-inf')
    for num in nums[64:67]:
        if num > max_num:
            max_num = num
    return max_num