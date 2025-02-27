def all_even_ints_exclusive(numbers):
    start = 28
    end = 53
    return [num for num in numbers[start:end] if num % 2 == 0]