def return_nth_smallest_ascii(s):
    ascii_values = [ord(char) for char in s if 20 <= s.index(char) <= 30]
    ascii_values.sort()
    if len(ascii_values) >= 8:
        return chr(ascii_values[7])
    else:
        return None