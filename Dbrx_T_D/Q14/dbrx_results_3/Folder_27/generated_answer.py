def find_second_smallest_num(numbers):
    if len(numbers) < 60:
        return None
    min_num1 = min(numbers[24:55])
    min_num2 = float('inf')
    for num in numbers[24:55]:
        if min_num1 < num < min_num2:
            min_num2 = num
    return min_num2 if min_num2 != float('inf') else None