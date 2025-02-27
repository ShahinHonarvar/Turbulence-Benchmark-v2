def return_nth_smallest_ascii(s):
    chars = [s[i] for i in range(52, 80)]
    ascii_values = [ord(c) for c in chars]
    unique_ascii_values = sorted(list(set(ascii_values)))
    return chr(unique_ascii_values[6])