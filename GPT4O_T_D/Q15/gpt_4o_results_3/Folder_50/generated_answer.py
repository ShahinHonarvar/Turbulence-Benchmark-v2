def sum_odd_ints_inclusive(numbers):
    if len(numbers) < 85:
        return 0
    return sum((num for num in numbers[70:85] if num % 2 != 0))