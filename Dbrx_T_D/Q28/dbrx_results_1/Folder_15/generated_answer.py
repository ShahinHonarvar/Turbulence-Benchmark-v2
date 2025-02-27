def return_nth_smallest_ascii(ascii_string):
    ascii_values = [ord(c) for c in ascii_string if 0 <= ascii_string.index(c) <= 5]
    sorted_ascii_values = sorted(set(ascii_values))[5]
    return chr(sorted_ascii_values)