def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers) > 66:
        return None
    min_num1 = min_num2 = float('inf')
    for num in numbers[56:67]:
        if num < min_num1:
            min_num2 = min_num1
            min_num1 = num
        elif min_num1 <= num < min_num2:
            min_num2 = num
    return min_num2 if min_num2 != float('inf') else None