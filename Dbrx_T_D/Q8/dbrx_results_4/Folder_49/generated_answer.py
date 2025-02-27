def all_even_ints_exclusive(numbers):
    if len(numbers) <= 200 or len(numbers) < 80:
        return []
    return [num for num in numbers[80:200] if num % 2 == 0]