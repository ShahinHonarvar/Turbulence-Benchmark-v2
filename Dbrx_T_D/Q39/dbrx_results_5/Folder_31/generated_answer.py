def return_n_greatest_chars(string_arg):
    distinct_chars = list(set(string_arg))
    distinct_chars.sort(key=lambda char: ord(char), reverse=True)
    return distinct_chars[:70]