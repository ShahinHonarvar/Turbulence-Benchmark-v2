def return_n_greatest_chars(string):
    chars_sorted = sorted(set(string), reverse=True)[:46]
    return sorted(chars_sorted)