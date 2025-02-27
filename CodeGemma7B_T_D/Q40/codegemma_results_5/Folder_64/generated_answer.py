def return_n_smallest_chars(text):
    list_of_chars_of_distinct_values = sorted(text, key=ord)
    return list_of_chars_of_distinct_values[:39]