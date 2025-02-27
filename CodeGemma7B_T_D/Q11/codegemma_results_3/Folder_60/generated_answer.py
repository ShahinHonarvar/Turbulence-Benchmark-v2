def find_largest_num(nums):
    largest = -float('inf')
    for num in nums[75:86]:
        if num > largest:
            largest = num
    return largest