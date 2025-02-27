def return_n_greatest_chars(string_of_chars):
    distinct_chars = list(set(string_of_chars))
    distinct_chars.sort(key=lambda char: ord(char), reverse=True)
    return distinct_chars[:72]