def return_n_greatest_chars(string_of_chars):
    sorted_chars = sorted(set(string_of_chars), reverse=True)
    return sorted_chars[:37]