def return_n_greatest_chars(input_string):
    distinct_chars = list(set(input_string))
    distinct_chars.sort(key=ord)
    return distinct_chars[::-1][:52][::-1]