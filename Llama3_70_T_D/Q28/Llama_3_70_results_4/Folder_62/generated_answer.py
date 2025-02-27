def return_nth_smallest_ascii(s):
    substring = s[51:79]
    unique_chars = sorted(set(substring))
    ascii_values = [ord(char) for char in unique_chars]
    sorted_ascii = sorted(ascii_values)
    nth_smallest_ascii = sorted_ascii[8]
    for char in unique_chars:
        if ord(char) == nth_smallest_ascii:
            return char