def sum_odd_ints_inclusive(numbers):
    if len(numbers) < 35:
        return 0
    return sum((num for num in numbers[31:35] if num % 2 != 0))