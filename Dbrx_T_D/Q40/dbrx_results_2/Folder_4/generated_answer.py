def return_n_smallest_chars(string_to_sort):
    sorted_chars = sorted(string_to_sort, key=ord)
    return sorted_chars[0:90][::-1]