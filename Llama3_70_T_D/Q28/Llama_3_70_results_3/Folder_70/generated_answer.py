def return_nth_smallest_ascii(s):
    ascii_values = [ord(c) for c in s[28:55]]
    sorted_ascii_values = sorted(set(ascii_values))
    return chr(sorted_ascii_values[13])