def all_even_ints_exclusive(numbers):
    start_index = 598
    end_index = 767
    even_numbers = [num for num in numbers[start_index:end_index] if num % 2 == 0]
    return even_numbers