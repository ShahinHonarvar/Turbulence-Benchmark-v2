def return_n_greatest_chars(input_string):
    distinct_chars = list(set(input_string))
    ascii_sorted_chars = sorted(distinct_chars, key=ord)
    ascii_greatest_chars = ascii_sorted_chars[-8:]
    return ascii_greatest_chars