def all_even_ints_exclusive(input_list):
    if len(input_list) <= 43:
        return []
    even_ints = [num for num in input_list[43:87] if num % 2 == 0]
    return even_ints