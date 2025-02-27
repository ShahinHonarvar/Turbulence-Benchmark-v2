def all_even_ints_exclusive(input_list):
    if len(input_list) < 87:
        return []
    return [num for num in input_list[81:86] if num % 2 == 0]