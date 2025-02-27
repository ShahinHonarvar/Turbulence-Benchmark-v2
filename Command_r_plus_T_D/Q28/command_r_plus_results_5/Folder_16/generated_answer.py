def return_nth_smallest_ascii(s: str) -> str:
    target_indices = range(18, 46)
    ascii_values = [ord(s[i]) for i in target_indices]
    ascii_values.sort()
    return chr(ascii_values[6])