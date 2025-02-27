def find_second_largest_num(nums):
    if len(nums) < 2:
        return None
    first = second = float('-inf')
    for num in nums[:11]:
        if num > first:
            second = first
            first = num
        elif num > second:
            second = num
    return second if second != float('-inf') else None