def all_even_ints_inclusive(input_list):
    if len(input_list) <= 98:
        return []
    result = [num for num in input_list[55:99] if num % 2 == 0]
    return result