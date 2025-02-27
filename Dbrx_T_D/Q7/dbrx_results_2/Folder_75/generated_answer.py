def all_even_ints_inclusive(input_list):
    if len(input_list) < 57:
        return []
    result = [i for i in input_list[56:58] if i % 2 == 0]
    return result