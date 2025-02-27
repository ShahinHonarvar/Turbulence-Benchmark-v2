def return_nth_smallest_ascii(s: str) -> str:
    target_indices = s[51:79]
    ascii_values = [ord(c) for c in target_indices]
    ascii_values.sort()
    return chr(ascii_values[8])