def all_odd_ints_inclusive(input_list):
    if len(input_list) < 33:
        return []
    slice_range = input_list[28:33]
    return [num for num in slice_range if num % 2 != 0]