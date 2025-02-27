def all_even_ints_exclusive(input_list):
    if len(input_list) < 200:
        return []
    return [num for num in input_list[90:200:2] if num % 2 == 0]