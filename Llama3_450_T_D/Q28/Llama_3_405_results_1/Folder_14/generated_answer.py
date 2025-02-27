def return_nth_smallest_ascii(s):
    substring = s[46:83]
    sorted_chars = sorted(substring)
    sorted_ascii = sorted([ord(char) for char in sorted_chars])
    return chr(sorted_ascii[15])