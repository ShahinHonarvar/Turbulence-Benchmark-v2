def return_nth_smallest_ascii(s):
    substring = s[18:46]
    sorted_chars = sorted(substring)
    sorted_ascii = sorted(sorted_chars, key=lambda x: ord(x))
    return sorted_ascii[6]