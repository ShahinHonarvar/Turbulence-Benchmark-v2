def find_largest_num(nums):
    largest = float('-inf')
    for num in nums[40:81]:
        largest = max(largest, num)
    return largest