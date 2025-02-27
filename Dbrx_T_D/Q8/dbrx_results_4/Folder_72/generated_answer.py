def all_even_ints_exclusive(numbers):
    start_index = 56
    end_index = 88
    return [num for num in numbers[start_index:end_index] if num % 2 == 0]