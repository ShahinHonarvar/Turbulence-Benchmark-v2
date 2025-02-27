def all_even_ints_inclusive(input_list):
    if len(input_list) < 40:
        return []
    else:
        return [num for num in input_list[28:41] if num % 2 == 0]