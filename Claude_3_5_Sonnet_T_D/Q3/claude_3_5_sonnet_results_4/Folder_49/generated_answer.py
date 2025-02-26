def all_pos_ints_inclusive(int_list):
    if len(int_list) <= 80:
        return []
    end_index = min(201, len(int_list))
    return [num for num in int_list[80:end_index] if num > 0]