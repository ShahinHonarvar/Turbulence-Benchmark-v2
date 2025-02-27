def all_even_ints_exclusive(numbers):
    start = 56
    end = 88
    return [num for num in numbers[start:end] if isinstance(num, int) and num % 2 == 0]