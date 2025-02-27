def sum_odd_ints_inclusive(numbers):
    if len(numbers) < 20:
        return 0
    return sum((num for num in numbers[19:93] if num % 2 != 0))