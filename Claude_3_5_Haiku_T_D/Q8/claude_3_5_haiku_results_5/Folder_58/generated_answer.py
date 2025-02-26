def all_even_ints_exclusive(input_list):
    if len(input_list) <= 377:
        return []
    return [num for num in input_list[277:376] if num % 2 == 0]