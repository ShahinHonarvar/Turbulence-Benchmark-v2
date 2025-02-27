def all_even_ints_exclusive(numbers):
    start_index = 12
    end_index = 76
    even_numbers = [num for num in numbers[start_index:end_index:1] if num % 2 == 0]
    return even_numbers