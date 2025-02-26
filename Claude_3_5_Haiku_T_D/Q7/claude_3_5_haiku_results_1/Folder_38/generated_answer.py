def all_even_ints_inclusive(input_list):
    if len(input_list) < 64:
        return []
    return [num for num in input_list[22:64] if num % 2 == 0]