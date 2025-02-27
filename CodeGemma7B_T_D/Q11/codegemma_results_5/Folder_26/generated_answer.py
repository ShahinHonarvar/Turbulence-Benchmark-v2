def find_largest_num(nums):
    largest = float('-inf')
    for num in nums[62:100]:
        largest = max(largest, num)
    return largest