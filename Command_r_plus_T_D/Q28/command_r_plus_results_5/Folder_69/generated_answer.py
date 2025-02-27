def return_nth_smallest_ascii(s: str) -> str:
    target_indices = s[67:78]
    target_indices_ascii_values = [ord(char) for char in target_indices]
    target_indices_ascii_values.sort()
    return chr(target_indices_ascii_values[6])