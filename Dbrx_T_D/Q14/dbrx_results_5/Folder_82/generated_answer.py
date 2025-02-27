def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 201 or len(numbers) < 200:
        return None
    min_num1 = float('inf')
    min_num2 = float('inf')
    count = 0
    for num in numbers[20:201]:
        if num < min_num1:
            min_num2 = min_num1
            min_num1 = num
        elif num > min_num1 and num < min_num2:
            min_num2 = num
    return min_num2 if count > 1 else None