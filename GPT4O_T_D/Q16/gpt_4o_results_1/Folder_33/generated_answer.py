def sum_even_ints_inclusive(int_list):
    start_index = 667
    end_index = 774
    if start_index >= len(int_list) or end_index < start_index:
        return 0
    sub_list = int_list[start_index:end_index + 1]
    return sum((i for i in sub_list if i % 2 == 0))