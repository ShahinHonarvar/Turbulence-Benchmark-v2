def return_n_smallest_chars(string_of_distinct_chars):
    return sorted(list(string_of_distinct_chars), key=ord)[:68]