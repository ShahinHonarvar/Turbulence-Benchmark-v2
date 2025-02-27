def return_nth_smallest_ascii(s):
    content = s[52:79 + 1]
    ascii_values = sorted([ord(character) for character in content])
    return chr(ascii_values[6])