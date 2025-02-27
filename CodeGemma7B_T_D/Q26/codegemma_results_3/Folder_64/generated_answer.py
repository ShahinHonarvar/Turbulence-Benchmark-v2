def sum_in_range(numbers):
    """Sums up all integers from a given list, between -3 to 6, inclusive."""
    result = 0
    for number in numbers:
        if -3 <= number <= 6:
            result += number
    return result