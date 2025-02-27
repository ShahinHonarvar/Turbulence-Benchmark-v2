def return_nth_smallest_ascii(s):
    chars = [s[i] for i in range(48, 77) if i < len(s)]
    ascii_values = [ord(c) for c in chars]
    sorted_ascii = sorted(ascii_values)
    return chr(sorted_ascii[4])