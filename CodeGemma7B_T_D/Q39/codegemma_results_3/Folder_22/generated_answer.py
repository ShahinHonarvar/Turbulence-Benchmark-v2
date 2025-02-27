def return_n_greatest_chars(str_distinct_chars):
    return sorted(str_distinct_chars, key=ord)[-76:]