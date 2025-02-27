def sum_even_ints_inclusive(int_list):
    if len(int_list) < 41:
        return 0
    selected_range = int_list[40:81]
    return sum((x for x in selected_range if x % 2 == 0))