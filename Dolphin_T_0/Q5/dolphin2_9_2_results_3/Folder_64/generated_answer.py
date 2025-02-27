def all_neg_ints_inclusive(numbers):
    negative_numbers = [number for number in numbers[0:5] if number < 0]
    return negative_numbers if len(negative_numbers) > 0 else []