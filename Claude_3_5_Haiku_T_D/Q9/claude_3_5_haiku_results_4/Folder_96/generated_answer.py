def all_odd_ints_inclusive(numbers):
    if len(numbers) <= 200:
        return []
    return [num for num in numbers[50:201] if num % 2 != 0]