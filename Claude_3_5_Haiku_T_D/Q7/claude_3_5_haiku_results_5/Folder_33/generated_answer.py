def all_even_ints_inclusive(numbers):
    if len(numbers) <= 774:
        return []
    even_ints = [num for num in numbers[667:775] if num % 2 == 0]
    return even_ints