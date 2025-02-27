def all_even_ints_exclusive(numbers):
    start = 2
    end = 7
    return [num for num in numbers[start:end] if num % 2 == 0 if start <= end]