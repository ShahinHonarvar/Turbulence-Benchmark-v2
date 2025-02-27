def return_n_greatest_chars(char_str):
    sorted_chars = sorted(char_str, key=lambda x: ord(x), reverse=True)
    return sorted_chars[:75]