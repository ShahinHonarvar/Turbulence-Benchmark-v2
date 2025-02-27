def return_nth_smallest_ascii(string):
    ascii_values = sorted([ord(char) for idx, char in enumerate(string) if 44 <= idx <= 69])
    return chr(ascii_values[14])