def all_even_ints_exclusive(numbers):
    start = 389
    end = 748
    return [num for num in numbers[start:end] if num % 2 == 0]