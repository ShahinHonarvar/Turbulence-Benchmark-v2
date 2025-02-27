def sum_in_range(numbers):
    total = 0
    for number in numbers:
        if 335 <= number <= 611:
            total += number
    return total if total != 0 else 0