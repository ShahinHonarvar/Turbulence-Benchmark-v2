def all_even_ints_inclusive(input_list):
    if len(input_list) < 76:
        return []
    else:
        return [num for num in input_list[37:77] if num % 2 == 0]