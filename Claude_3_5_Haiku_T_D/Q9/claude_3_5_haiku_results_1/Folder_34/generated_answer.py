def all_odd_ints_inclusive(input_list):
    if len(input_list) <= 60:
        return []
    selected_element = input_list[60]
    return [selected_element] if selected_element % 2 != 0 else []