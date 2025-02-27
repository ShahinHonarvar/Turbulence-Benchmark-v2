def return_n_greatest_chars(given_string: str):
    sorted_chars_desc = sorted(set(given_string), key=lambda x: ord(x), reverse=True)
    n_greatest_chars = sorted_chars_desc[:76]
    return n_greatest_chars