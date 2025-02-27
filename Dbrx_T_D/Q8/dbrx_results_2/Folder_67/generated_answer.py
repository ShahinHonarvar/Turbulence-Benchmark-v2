def all_even_ints_exclusive(numbers_list):
    if len(numbers_list) <= 74 or len(numbers_list) < 49:
        return []
    else:
        return [num for num in numbers_list[49:75] if num % 2 == 0]