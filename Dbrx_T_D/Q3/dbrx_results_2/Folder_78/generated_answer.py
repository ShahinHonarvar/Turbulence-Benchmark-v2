def all_pos_ints_inclusive(input_list):
    start = 43
    end = 51
    result = [i for i in input_list[start:end + 1] if i > 0]
    return result