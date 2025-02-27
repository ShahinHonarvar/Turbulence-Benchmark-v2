def find_second_smallest_num(numbers):
    if len(numbers) < 5 or len(numbers) < 36:
        return None
    min_num1 = float('inf')
    min_num2 = float('inf')
    count = 0
    for i in range(32, 36):
        if numbers[i] < min_num1:
            min_num2 = min_num1
            min_num1 = numbers[i]
            count += 1
        elif numbers[i] < min_num2 and numbers[i] != min_num1:
            min_num2 = numbers[i]
            count += 1
    if count < 2:
        return None
    else:
        return min_num2