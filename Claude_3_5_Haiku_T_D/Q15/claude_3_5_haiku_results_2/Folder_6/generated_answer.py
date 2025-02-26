def sum_odd_ints_inclusive(numbers):
    if len(numbers) <= 66:
        return 0
    return sum((num for num in numbers[10:67] if num % 2 != 0))