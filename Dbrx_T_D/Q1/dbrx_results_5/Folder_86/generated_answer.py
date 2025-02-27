def all_ints_inclusive(numbers):
    if len(numbers) >= 80:
        return numbers[40:81]
    else:
        return numbers[-41:] if len(numbers) >= 41 else []