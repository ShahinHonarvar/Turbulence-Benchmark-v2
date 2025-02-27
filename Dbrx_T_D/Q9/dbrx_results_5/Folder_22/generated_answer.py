def all_odd_ints_inclusive(numbers):
    if len(numbers) < 201:
        return []
    elif len(numbers) < 40:
        return [n for n in numbers[40:201] if n % 2 != 0]
    else:
        return [n for n in numbers[40:201] if n % 2 != 0]