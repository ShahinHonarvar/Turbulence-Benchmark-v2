def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers[52:72]) < 2:
        return None
    min_num = min_num2 = float('inf')
    for num in numbers[52:72]:
        if num < min_num:
            min_num2 = min_num
            min_num = num
        elif min_num < num < min_num2:
            min_num2 = num
    return min_num2