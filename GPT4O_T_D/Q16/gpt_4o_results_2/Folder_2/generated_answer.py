def sum_even_ints_inclusive(numbers):
    if len(numbers) < 40:
        return 0
    even_sum = sum((num for num in numbers[15:40] if num % 2 == 0))
    return even_sum