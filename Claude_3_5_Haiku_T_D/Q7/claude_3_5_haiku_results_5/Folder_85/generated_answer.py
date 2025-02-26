def all_even_ints_inclusive(numbers):
    if len(numbers) < 9:
        return []
    even_sublist = [num for num in numbers[6:9] if num % 2 == 0]
    return even_sublist