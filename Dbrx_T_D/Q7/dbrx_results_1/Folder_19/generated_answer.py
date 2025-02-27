def all_even_ints_inclusive(numbers):
    start_index = 3
    end_index = 5
    even_integers = [num for num in numbers[start_index:end_index + 1] if num % 2 == 0]
    return even_integers