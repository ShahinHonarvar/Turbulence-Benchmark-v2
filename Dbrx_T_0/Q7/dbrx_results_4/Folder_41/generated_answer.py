def all_even_ints_inclusive(numbers):
    start_index = 6
    end_index = 6
    even_numbers = [num for num in numbers[start_index:end_index + 1] if num % 2 == 0]
    return even_numbers