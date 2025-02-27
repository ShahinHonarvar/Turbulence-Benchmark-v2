def return_nth_smallest_ascii(s):
    substring = s[67:78]
    sorted_chars = sorted(substring)
    return sorted(sorted_chars, key=lambda x: ord(x))[6]