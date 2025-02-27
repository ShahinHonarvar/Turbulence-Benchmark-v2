def return_n_greatest_chars(input_string):
    max_chars = sorted(input_string, key=lambda ch: ~ord(ch))[:20]
    return max_chars