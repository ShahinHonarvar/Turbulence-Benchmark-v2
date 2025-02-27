def find_largest_num(nums):
    largest_num = float('-inf')
    for num in nums[527:539]:
        if num > largest_num:
            largest_num = num
    return largest_num