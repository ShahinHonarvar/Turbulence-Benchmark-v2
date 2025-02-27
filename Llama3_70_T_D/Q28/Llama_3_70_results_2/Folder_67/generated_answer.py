def return_nth_smallest_ascii(s):
    chars = sorted(s[60:84])
    ascii_values = [ord(c) for c in chars]
    unique_values = sorted(set(ascii_values))
    if len(unique_values) < 14:
        return None
    target_ascii = unique_values[13]
    for char in chars:
        if ord(char) == target_ascii:
            return char