def all_even_ints_exclusive(input_list):
    if len(input_list) <= 19:
        return []
    subset = input_list[19:37]
    return [num for num in subset if num % 2 == 0]