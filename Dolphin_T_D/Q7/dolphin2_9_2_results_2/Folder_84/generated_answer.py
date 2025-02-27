def all_even_ints_inclusive(numbers):
    result = [num for num in numbers[43:87] if num % 2 == 0]
    return result if result else []