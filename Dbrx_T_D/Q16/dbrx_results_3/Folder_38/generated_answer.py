def sum_even_ints_inclusive(int_list):
    start_index = 22
    end_index = 63
    sub_list = int_list[start_index:end_index + 1]
    even_sub_list = [i for i in sub_list if i % 2 == 0]
    return sum(even_sub_list) if even_sub_list else 0