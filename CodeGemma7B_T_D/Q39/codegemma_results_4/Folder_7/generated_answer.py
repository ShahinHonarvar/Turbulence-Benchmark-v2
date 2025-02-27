def return_n_greatest_chars(given_str):
    sorted_list = sorted(given_str, key=ord)
    return sorted_list[-49:]