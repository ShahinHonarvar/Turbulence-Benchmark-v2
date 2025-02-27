def return_nth_smallest_ascii(s):
    target_chars = s[44:70]
    ascii_values = [ord(c) for c in target_chars]
    unique_values = sorted(set(ascii_values))
    return chr(unique_values[14])