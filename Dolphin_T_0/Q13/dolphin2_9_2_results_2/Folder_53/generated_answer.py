def find_second_largest_num(nums):
    if not nums:
        return None
    nums = nums[100:201]
    if len(nums) <= 1:
        return None
    first = second = float('-inf')
    for num in nums:
        if num > first:
            first, second = (num, first)
        elif first > num > second:
            second = num
    if second == float('-inf'):
        return None
    return second