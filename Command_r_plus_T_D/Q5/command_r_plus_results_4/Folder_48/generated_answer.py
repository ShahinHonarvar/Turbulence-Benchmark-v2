def all_neg_ints_inclusive(int_list):
    start_index = 533
    end_index = 605
    if end_index >= len(int_list):
        end_index = len(int_list) - 1
    return [i for i in int_list[start_index:end_index + 1] if i < 0]