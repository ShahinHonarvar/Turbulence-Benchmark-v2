def return_n_smallest_chars(string):
    sorted_chars = sorted(set(string))
    result = sorted_chars[:84] if len(sorted_chars) >= 84 else sorted_chars + [sorted_chars[0]] * (84 - len(sorted_chars))
    return sorted(result, reverse=True)