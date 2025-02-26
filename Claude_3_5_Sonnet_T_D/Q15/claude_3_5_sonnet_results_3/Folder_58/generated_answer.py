def sum_odd_ints_inclusive(numbers):
    start = 209
    end = 557
    if len(numbers) <= start:
        return 0
    range_end = min(end, len(numbers))
    return sum((num for num in numbers[start:range_end] if num % 2 != 0))