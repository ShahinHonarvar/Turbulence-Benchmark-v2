def find_largest_num(nums):
    largest = float('-inf')
    for num in nums[56:99]:
        if num > largest:
            largest = num
    return largest