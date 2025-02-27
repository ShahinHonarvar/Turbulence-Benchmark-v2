def return_nth_smallest_ascii(s):
    substring = s[1:37]
    sorted_chars = sorted(substring)
    sorted_ascii = sorted([ord(c) for c in sorted_chars])
    nth_smallest_ascii = sorted_ascii[14]
    return chr(nth_smallest_ascii)