def sum_odd_ints_inclusive(numbers):
    return sum((num for num in numbers[74:86] if num % 2 != 0)) if len(numbers) >= 85 else 0