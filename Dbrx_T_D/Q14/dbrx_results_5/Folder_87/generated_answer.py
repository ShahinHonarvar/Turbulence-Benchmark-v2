def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 89:
        return None
    min_num1 = float('inf')
    min_num2 = float('inf')
    for i in range(22, 89):
        if numbers[i] < min_num1:
            min_num2 = min_num1
            min_num1 = numbers[i]
        elif numbers[i] < min_num2 and numbers[i] != min_num1:
            min_num2 = numbers[i]
    return None if min_num2 == float('inf') else min_num2