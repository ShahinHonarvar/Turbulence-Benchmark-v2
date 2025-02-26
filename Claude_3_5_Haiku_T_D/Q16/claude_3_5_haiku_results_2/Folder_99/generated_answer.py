def sum_even_ints_inclusive(numbers):
    if len(numbers) <= 370:
        return 0
    even_sum = sum((num for num in numbers[310:371] if num % 2 == 0))
    return even_sum