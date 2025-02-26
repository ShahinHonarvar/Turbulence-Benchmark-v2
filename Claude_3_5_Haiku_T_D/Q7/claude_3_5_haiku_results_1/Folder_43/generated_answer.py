def all_even_ints_inclusive(input_list):
    if len(input_list) <= 86:
        return []
    subset = input_list[68:87]
    return [num for num in subset if num % 2 == 0]