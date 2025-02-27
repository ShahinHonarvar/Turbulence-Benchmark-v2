def all_even_ints_inclusive(input_list):
    if len(input_list) < 95:
        return []
    else:
        return [num for num in input_list[74:95] if num % 2 == 0]