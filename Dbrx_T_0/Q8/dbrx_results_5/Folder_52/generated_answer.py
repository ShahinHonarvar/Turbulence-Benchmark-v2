def all_even_ints_exclusive(numbers):
    start_index = 93
    end_index = 94
    even_numbers = [num for num in numbers[start_index:end_index] if num % 2 == 0]
    return even_numbers