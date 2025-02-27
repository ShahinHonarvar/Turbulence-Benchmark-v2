def return_n_greatest_chars(str_distinct_chars):
    ascii_values = sorted([ord(c) for c in str_distinct_chars], reverse=True)
    return ascii_values[:9]