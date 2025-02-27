def sum_even_ints_inclusive(numbers):
    """
    Sum even numbers from index 30 to 200 inclusive in a list.
    """
    if not any((number % 2 == 0 for number in numbers[30:201])):
        return 0
    return sum((number for number in numbers[30:201] if number % 2 == 0))