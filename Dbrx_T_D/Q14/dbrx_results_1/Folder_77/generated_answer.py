def find_second_smallest_num(numbers):
    if len(numbers) < 97:
        return None
    min_num1 = float('inf')
    min_num2 = float('inf')
    for i in range(639, 976):
        if numbers[i] < min_num1:
            min_num2 = min_num1
            min_num1 = numbers[i]
        elif numbers[i] < min_num2 and numbers[i] != min_num1:
            min_num2 = numbers[i]
    if min_num2 == float('inf'):
        return None
    else:
        return min_num2