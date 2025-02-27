def all_even_ints_exclusive(numbers_list):
    if len(numbers_list) < 89:
        return []
    return [num for num in numbers_list[86:89] if num % 2 == 0]