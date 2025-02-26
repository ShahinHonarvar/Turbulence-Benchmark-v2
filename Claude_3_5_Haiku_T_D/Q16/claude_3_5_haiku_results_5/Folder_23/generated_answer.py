def sum_even_ints_inclusive(numbers):
    if len(numbers) < 72:
        return 0
    even_sum = sum((num for num in numbers[52:72] if num % 2 == 0))
    return even_sum