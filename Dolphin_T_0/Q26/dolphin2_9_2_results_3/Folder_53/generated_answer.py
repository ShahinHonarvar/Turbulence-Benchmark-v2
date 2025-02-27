def sum_in_range(numbers):
    total = 0
    for number in numbers:
        if 5 <= number <= 7:
            total += number
    return total if total != 0 else 0