def return_n_greatest_chars(distinct_char_string):
    sorted_chars = sorted(distinct_char_string, reverse=True)
    return sorted(sorted_chars[:24])