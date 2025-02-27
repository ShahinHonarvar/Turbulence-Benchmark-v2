def find_second_largest_num(nums):
    if len(nums) < 2:
        return None
    max_num1 = float('-inf')
    max_num2 = float('-inf')
    for num in nums:
        if num > max_num1:
            max_num2 = max_num1
            max_num1 = num
        elif num > max_num2 and num < max_num1:
            max_num2 = num
    return max_num2