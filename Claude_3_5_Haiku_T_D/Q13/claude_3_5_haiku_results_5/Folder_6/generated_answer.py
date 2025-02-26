def find_second_largest_num(numbers):
    if len(numbers) < 67:
        return None
    subset = numbers[10:67]
    if len(subset) < 2:
        return None
    max_num = float('-inf')
    second_max_num = float('-inf')
    for num in subset:
        if num > max_num:
            second_max_num = max_num
            max_num = num
        elif num > second_max_num and num != max_num:
            second_max_num = num
    return second_max_num if second_max_num != float('-inf') else None