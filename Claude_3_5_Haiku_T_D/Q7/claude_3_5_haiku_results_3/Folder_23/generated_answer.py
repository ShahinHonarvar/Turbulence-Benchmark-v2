def all_even_ints_inclusive(input_list):
    if len(input_list) <= 71:
        return []
    selected_range = input_list[52:72]
    return [num for num in selected_range if num % 2 == 0]