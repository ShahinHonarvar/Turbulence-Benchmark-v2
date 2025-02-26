def all_even_ints_inclusive(numbers):
    if len(numbers) <= 80:
        return []
    even_numbers = [num for num in numbers[40:81] if num % 2 == 0]
    return even_numbers