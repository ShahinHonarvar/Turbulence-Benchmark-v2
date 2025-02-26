def all_odd_ints_inclusive(input_list):
    if len(input_list) <= 750:
        return []
    return [num for num in input_list[246:751] if num % 2 != 0]