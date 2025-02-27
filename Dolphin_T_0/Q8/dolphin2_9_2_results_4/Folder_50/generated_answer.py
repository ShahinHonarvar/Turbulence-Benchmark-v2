def all_even_ints_exclusive(numbers):
    range_start = 70
    range_end = 98
    return [num for num in numbers[range_start:range_end] if num % 2 == 0]