def all_even_ints_exclusive(numbers):
    start = 56
    end = 92
    even_numbers = [num for num in numbers[start:end] if num % 2 == 0]
    return even_numbers