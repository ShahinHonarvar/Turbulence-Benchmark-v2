def return_n_greatest_chars(string_):
    ascii_sorted_list = sorted(list(set(string_)), key=ord)
    n_greatest_ascii_values_list = ascii_sorted_list[-73:]
    return sorted(n_greatest_ascii_values_list)