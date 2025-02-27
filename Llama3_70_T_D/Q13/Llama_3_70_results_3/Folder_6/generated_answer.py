def find_second_largest_num(numbers):
    if len(numbers) < 67:
        return None
    second_largest = float('-inf')
    max_num = float('-inf')
    for num in numbers[10:67]:
        if num > max_num:
            second_largest = max_num
            max_num = num
        elif num > second_largest and num != max_num:
            second_largest = num
    return second_largest if second_largest != float('-inf') else None