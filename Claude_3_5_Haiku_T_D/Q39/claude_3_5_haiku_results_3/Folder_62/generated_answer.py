def return_n_greatest_chars(string):
    sorted_chars = sorted(set(string), reverse=True)
    return sorted_chars[:84] if len(sorted_chars) >= 84 else sorted_chars