def all_even_ints_inclusive(numbers):
    if len(numbers) <= 57:
        return []
    even_nums = [num for num in numbers[56:58] if num % 2 == 0]
    return even_nums