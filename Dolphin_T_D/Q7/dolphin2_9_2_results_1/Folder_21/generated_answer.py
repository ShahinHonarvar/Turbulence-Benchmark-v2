def all_even_ints_inclusive(numbers):
    range_numbers = numbers[639:976]
    even_numbers = [num for num in range_numbers if num % 2 == 0]
    return even_numbers