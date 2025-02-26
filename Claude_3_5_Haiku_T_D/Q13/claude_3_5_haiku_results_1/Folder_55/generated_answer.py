def find_second_largest_num(numbers):
    if len(numbers) <= 1 or len(numbers) < 11:
        return None
    max_num = float('-inf')
    second_max_num = float('-inf')
    for i in range(11):
        if numbers[i] > max_num:
            second_max_num = max_num
            max_num = numbers[i]
        elif numbers[i] > second_max_num and numbers[i] != max_num:
            second_max_num = numbers[i]
    return second_max_num if second_max_num != float('-inf') else None