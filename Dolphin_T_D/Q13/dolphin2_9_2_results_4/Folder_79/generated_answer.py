def find_second_largest_num(nums):
    if len(nums) < 2:
        return None
    first = second = float('-inf')
    for num in nums:
        if num <= first:
            first = num
        elif num < second:
            second = num
    if second == float('-inf'):
        return None
    return second