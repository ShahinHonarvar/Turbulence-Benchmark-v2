def return_n_greatest_chars(string_of_chars):
    distinct_chars = list(set(string_of_chars))
    total_chars = len(distinct_chars)
    if total_chars < 14:
        return sorted(distinct_chars, reverse=True)
    else:
        return sorted(distinct_chars, key=ord, reverse=True)[:14]