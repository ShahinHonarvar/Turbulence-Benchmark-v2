def return_n_smallest_chars(string_of_chars):
    sorted_chars = sorted(list(string_of_chars))[:59]
    sorted_chars.sort(reverse=True)
    return sorted_chars