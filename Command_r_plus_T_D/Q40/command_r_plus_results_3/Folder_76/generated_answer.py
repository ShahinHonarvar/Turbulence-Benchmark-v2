def return_n_smallest_chars(input_string):
    smallest_chars = sorted(input_string)[:3]
    smallest_chars.sort(reverse=True)
    return smallest_chars