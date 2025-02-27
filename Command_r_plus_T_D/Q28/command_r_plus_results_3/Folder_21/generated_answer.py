def return_nth_smallest_ascii(s: str) -> str:
    target_indices = s[8:66]
    ascii_values = [ord(char) for char in target_indices]
    sorted_ascii = sorted(ascii_values)
    sixth_smallest_ascii = sorted_ascii[5]
    nth_smallest_char = chr(sixth_smallest_ascii)
    return nth_smallest_char