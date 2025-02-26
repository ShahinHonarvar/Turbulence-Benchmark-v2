def all_odd_ints_inclusive(input_list):
    if len(input_list) < 95:
        return []
    slice_range = input_list[75:95]
    odd_integers = [num for num in slice_range if num % 2 != 0]
    return odd_integers