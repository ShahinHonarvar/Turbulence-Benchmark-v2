def find_second_largest_num(numbers):
    if not numbers or len(numbers) < 775:
        return None
    target_numbers = numbers[667:775]
    max_num = second_max_num = float('-inf')
    for num in target_numbers:
        if num > max_num:
            second_max_num = max_num
            max_num = num
        elif num > second_max_num and num < max_num:
            second_max_num = num
    return second_max_num if second_max_num != float('-inf') else None