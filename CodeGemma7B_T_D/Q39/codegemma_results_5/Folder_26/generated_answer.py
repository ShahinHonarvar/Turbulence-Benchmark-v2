def return_n_greatest_chars(given_string):
    sorted_list_of_chars = sorted(given_string, key=ord, reverse=True)[:43]
    return sorted_list_of_chars