def return_nth_smallest_ascii(s):
    s = s[62:84]
    unique_chars = sorted(set(s))
    ascii_values = [ord(char) for char in unique_chars]
    sorted_ascii_values = sorted(ascii_values)
    ninth_smallest_ascii = sorted_ascii_values[8]
    for char in unique_chars:
        if ord(char) == ninth_smallest_ascii:
            return char