def find_second_smallest_num(numbers):
    if len(numbers) < 5:
        return None
    min_num1 = min(numbers[4:5])
    min_num2 = None
    for num in numbers[4:]:
        if num > min_num1:
            if min_num2 is None or num < min_num2:
                min_num2 = num
    return min_num2 if min_num2 is not None else None