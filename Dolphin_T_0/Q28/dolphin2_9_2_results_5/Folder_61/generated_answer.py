def return_nth_smallest_ascii(string):
    ascii_values = [ord(ch) for ch in string[0:10]]
    sorted_values = sorted(ascii_values)
    return chr(sorted_values[9])