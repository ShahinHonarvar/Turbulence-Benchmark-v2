def all_even_ints_inclusive(int_list):
    if len(int_list) <= 774:
        return []
    selected_range = int_list[667:775]
    return [num for num in selected_range if num % 2 == 0]