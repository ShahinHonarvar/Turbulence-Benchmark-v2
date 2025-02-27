def find_second_largest_num(nums):
    if len(nums) < 2:
        return None
    first, second = (nums[0], float('-inf'))
    for num in nums[1:]:
        if num > first:
            second = first
            first = num
        elif num > second:
            second = num
    return second if second != float('-inf') else None