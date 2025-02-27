def return_n_greatest_chars(distinct_chars):
    return sorted(distinct_chars, key=ord, reverse=True)[:21]