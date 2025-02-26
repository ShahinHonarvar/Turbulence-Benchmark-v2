def all_odd_ints_exclusive(input_list):
    if len(input_list) <= 94:
        return []
    return [num for num in input_list[79:93] if num % 2 != 0]