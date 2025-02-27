def return_n_greatest_chars(str_of_distinct_chars):
    return sorted(str_of_distinct_chars, key=ord, reverse=True)[:45]