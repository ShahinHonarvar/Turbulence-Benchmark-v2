def find_second_largest_num(numbers):
    nums = numbers[15:40]
    if len(nums) < 2:
        return None
    max_num = second_max = float('-inf')
    for num in nums:
        if num > max_num:
            second_max = max_num
            max_num = num
        elif num > second_max and num != max_num:
            second_max = num
    return second_max if second_max != float('-inf') else None