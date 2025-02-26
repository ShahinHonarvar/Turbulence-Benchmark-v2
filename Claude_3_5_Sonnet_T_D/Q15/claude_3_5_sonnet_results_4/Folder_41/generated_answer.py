def sum_odd_ints_inclusive(numbers):
    if len(numbers) < 7:
        return 0
    return sum((num for num in [numbers[6]] if num % 2 != 0))