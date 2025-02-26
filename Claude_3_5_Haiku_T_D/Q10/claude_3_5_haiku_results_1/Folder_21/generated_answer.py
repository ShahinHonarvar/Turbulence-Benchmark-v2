def all_odd_ints_exclusive(input_list):
    if len(input_list) <= 868:
        return []
    return [num for num in input_list[744:868] if num % 2 != 0]