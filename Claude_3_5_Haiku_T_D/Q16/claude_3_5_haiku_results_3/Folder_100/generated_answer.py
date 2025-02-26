def sum_even_ints_inclusive(numbers):
    if len(numbers) <= 68:
        return 0
    even_sum = sum((num for num in numbers[42:69] if num % 2 == 0))
    return even_sum