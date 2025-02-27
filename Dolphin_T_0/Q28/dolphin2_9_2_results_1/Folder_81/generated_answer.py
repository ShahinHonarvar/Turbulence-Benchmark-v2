def return_nth_smallest_ascii(string):
    ascii_values = [ord(ch) for ch in string]
    return chr(sorted(ascii_values[:14])[13])