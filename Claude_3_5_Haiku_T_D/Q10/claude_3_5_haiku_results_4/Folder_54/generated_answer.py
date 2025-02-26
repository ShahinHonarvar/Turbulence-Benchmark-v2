def all_odd_ints_exclusive(input_list):
    if len(input_list) <= 35:
        return []
    odd_ints = [num for num in input_list[28:34] if num % 2 != 0]
    return odd_ints