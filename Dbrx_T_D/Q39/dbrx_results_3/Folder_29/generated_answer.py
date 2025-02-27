def return_n_greatest_chars(input_string):
    distinct_chars = list(set(input_string))
    sorted_chars = sorted(distinct_chars, reverse=True)
    return sorted_chars[:23]