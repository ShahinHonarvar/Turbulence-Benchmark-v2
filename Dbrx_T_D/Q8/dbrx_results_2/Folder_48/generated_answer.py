def all_even_ints_exclusive(input_list):
    if len(input_list) < 999:
        return []
    result = [i for i in input_list[385:999] if i % 2 == 0]
    return result