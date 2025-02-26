def all_pos_ints_inclusive(input_list):
    if len(input_list) <= 27:
        return []
    end_index = min(55, len(input_list) - 1)
    selected_range = input_list[27:end_index + 1]
    return [num for num in selected_range if num > 0]