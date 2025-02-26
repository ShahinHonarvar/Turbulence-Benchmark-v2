def all_odd_ints_exclusive(input_list):
    if len(input_list) <= 984:
        return []
    return [num for num in input_list[370:983] if num % 2 != 0]