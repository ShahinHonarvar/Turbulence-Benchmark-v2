def return_nth_smallest_ascii(string):
    relevant_chars = string[62:84]
    ascii_values = [ord(c) for c in relevant_chars]
    sorted_values = sorted(ascii_values)
    return chr(sorted_values[8])