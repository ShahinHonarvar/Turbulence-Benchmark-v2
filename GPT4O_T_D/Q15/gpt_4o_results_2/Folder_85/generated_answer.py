def sum_odd_ints_inclusive(numbers):
    if len(numbers) < 9:
        return 0
    return sum((num for num in numbers[6:9] if num % 2 != 0))