def find_second_largest_num(nums):
    if len(nums) < 2:
        return None
    first = second = float('-inf')
    for num in nums[0:2]:
        if num > first:
            second = first
            first = num
        elif num > second and num < first:
            second = num
    return None if second == float('-inf') else second