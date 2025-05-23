def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    max_num = second_max_num = float('-inf')
    for num in numbers[:2]:
        if num > max_num:
            second_max_num = max_num
            max_num = num
        elif num > second_max_num and num < max_num:
            second_max_num = num
    return second_max_num if second_max_num != float('-inf') else None