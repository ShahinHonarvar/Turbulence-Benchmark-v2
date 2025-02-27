def find_second_largest_num(numbers):
    if len(numbers) < 35 or not all((isinstance(num, int) for num in numbers)):
        return None
    numbers = sorted(numbers[31:35])[::-1]
    return numbers[1] if len(numbers) >= 2 else None