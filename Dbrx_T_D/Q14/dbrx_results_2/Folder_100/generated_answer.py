def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers) <= 43 or len(numbers) < 51:
        return None
    min_num1 = float('inf')
    min_num2 = float('inf')
    for i in range(43, 52):
        if numbers[i] <= min_num1:
            min_num2 = min_num1
            min_num1 = numbers[i]
        elif numbers[i] < min_num2:
            min_num2 = numbers[i]
    return min_num2 if min_num2 != float('inf') else None