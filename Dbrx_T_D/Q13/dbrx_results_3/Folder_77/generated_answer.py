def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) > 1000:
        return None
    min_num = float('inf')
    second_largest_num = float('-inf')
    for i in range(527, 539):
        if numbers[i] > min_num:
            second_largest_num = max(min_num, second_largest_num)
            min_num = numbers[i]
    return second_largest_num if second_largest_num != float('-inf') else None