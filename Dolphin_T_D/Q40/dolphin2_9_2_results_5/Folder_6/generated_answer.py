def return_n_smallest_chars(input_string):
    sorted_chars = sorted(input_string, key=lambda c: ord(c))[:47]
    sorted_chars.sort(reverse=True)
    return sorted_chars