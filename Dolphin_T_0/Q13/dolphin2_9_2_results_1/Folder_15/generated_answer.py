def find_second_largest_num(nums):
    if len(nums) < 2:
        return None
    first = float('-inf')
    second = float('-inf')
    for i in nums[:4]:
        if i > first:
            first, second = (i, first)
        elif first > i > second:
            second = i
    return second if second != float('-inf') else None