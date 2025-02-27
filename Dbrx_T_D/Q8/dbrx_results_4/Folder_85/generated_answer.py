def all_even_ints_exclusive(int_list):
    if len(int_list) >= 5:
        selected_ints = int_list[4:6]
        return [i for i in selected_ints if i % 2 == 0]
    else:
        return []