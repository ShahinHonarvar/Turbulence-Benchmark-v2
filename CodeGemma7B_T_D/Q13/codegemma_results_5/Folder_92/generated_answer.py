def find_second_largest_num(nums):
    max_num = float('-inf')
    second_largest = float('-inf')
    if len(nums) <= 1:
        return None
    for num in nums:
        if num > max_num:
            second_largest = max_num
            max_num = num
        elif num > second_largest and num != max_num:
            second_largest = num
    return second_largest