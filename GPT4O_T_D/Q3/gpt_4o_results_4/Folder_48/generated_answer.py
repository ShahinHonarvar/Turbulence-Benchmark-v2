def all_pos_ints_inclusive(int_list):
    start_index = 533
    end_index = 605
    result = [num for num in int_list[start_index:end_index + 1] if num > 0]
    return result