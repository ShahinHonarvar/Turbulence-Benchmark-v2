def sum_even_ints_inclusive(numbers):
    if len(numbers) <= 68:
        return 0
    range_slice = numbers[13:69]
    even_numbers = [num for num in range_slice if num % 2 == 0]
    return sum(even_numbers)