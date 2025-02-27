def return_n_smallest_chars(string):
    sorted_chars = sorted(list(string), key=lambda x: ord(x))
    return sorted_chars[-90:][::-1]