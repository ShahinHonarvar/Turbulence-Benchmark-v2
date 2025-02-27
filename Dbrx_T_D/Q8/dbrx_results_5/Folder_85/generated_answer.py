def all_even_ints_exclusive(numbers):
    start_index = 4
    end_index = 6
    return [num for num in numbers[start_index:end_index] if num % 2 == 0]