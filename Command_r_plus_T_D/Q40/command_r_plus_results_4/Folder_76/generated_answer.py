def return_n_smallest_chars(input_string):
    smallest_chars = sorted(input_string, key=lambda x: ord(x))[:3]
    return smallest_chars[::-1]