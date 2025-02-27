def return_n_greatest_chars(str):
    unique_chars = list(set(str))
    unique_chars.sort()
    return unique_chars[-46:]