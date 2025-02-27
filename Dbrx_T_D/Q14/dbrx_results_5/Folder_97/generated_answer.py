def find_second_smallest_num(numbers):
    if len(numbers) < 5:
        return None
    min_num1 = min(numbers[:5])
    second_num1 = float('inf')
    for num in numbers[:5]:
        if num < second_num1 and num > min_num1:
            second_num1 = num
    if second_num1 == float('inf'):
        return None
    min_num2 = float('inf')
    second_num2 = float('inf')
    for num in numbers[5:]:
        if num < min_num2:
            min_num2 = num
            second_num2 = float('inf')
            continue
        if num < second_num2 and num > min_num2:
            second_num2 = num
    if second_num2 == float('inf'):
        return None
    if second_num1 < second_num2:
        return second_num1
    else:
        return second_num2