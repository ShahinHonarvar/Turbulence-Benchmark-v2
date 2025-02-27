def find_second_largest_num(nums):
    if not nums:
        return None
    if len(nums) < 2:
        return None
    first = second = float('-inf')
    for i in range(len(nums)):
        if 13 <= i <= 68:
            if nums[i] > first:
                second = first
                first = nums[i]
            elif first > nums[i] > second:
                second = nums[i]
    if second == float('-inf'):
        return None
    return second