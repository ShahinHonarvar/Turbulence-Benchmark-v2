def all_even_ints_inclusive(numbers_list):
    return [num for i, num in enumerate(numbers_list[30:88]) if num % 2 == 0 and i >= 30]