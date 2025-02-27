def all_even_ints_inclusive(input_list):
    if len(input_list) < 55:
        return []
    return [i for i in input_list[50:55] if i % 2 == 0]