def return_n_smallest_chars(s):
    char_list = sorted(set(s))[:80]
    return char_list + [''] * (80 - len(char_list))