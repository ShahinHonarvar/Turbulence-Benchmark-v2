def sum_odd_ints_inclusive(numbers):
    if len(numbers) <= 56:
        return 0
    end_index = min(83, len(numbers))
    return sum((num for num in numbers[56:end_index] if num % 2 != 0))