def return_n_smallest_chars(string_of_chars):
    sorted_chars = sorted(string_of_chars, key=ord)
    n_smallest_chars = sorted_chars[-79:]
    n_smallest_chars.sort(reverse=True)
    return n_smallest_chars