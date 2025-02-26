def return_n_greatest_chars(s):
    chars_sorted_desc = sorted(set(s), reverse=True)
    return sorted(chars_sorted_desc[:45])