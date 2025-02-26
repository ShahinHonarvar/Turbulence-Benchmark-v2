def all_even_ints_inclusive(numbers):
    if len(numbers) < 7:
        return []
    even_ints = [num for num in numbers[6:7] if num % 2 == 0]
    return even_ints