def all_even_ints_inclusive(input_list):
    if len(input_list) < 65:
        return []
    else:
        return [num for num in input_list[14:65] if num % 2 == 0]