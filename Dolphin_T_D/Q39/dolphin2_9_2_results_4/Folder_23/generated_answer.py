def return_n_greatest_chars(string_chars):
    return sorted([''.join(sorted(set(string_chars), reverse=True)[:46])])