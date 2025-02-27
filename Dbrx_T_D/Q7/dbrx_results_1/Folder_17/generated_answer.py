def all_even_ints_inclusive(input_list):
    if len(input_list) <= 78 or len(input_list) < 62:
        return []
    return [num for num in input_list[62:79] if num % 2 == 0]