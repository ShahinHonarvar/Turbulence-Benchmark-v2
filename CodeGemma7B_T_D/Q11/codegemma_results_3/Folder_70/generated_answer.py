def find_largest_num(nums):
    largest = float('-inf')
    for num in nums[28:33]:
        if num > largest:
            largest = num
    return largest