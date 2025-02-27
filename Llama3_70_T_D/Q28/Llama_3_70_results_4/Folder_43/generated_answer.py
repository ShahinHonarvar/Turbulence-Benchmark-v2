def return_nth_smallest_ascii(s):
    substring = s[14:36]
    unique_chars = list(set(substring))
    unique_chars.sort(key=lambda x: ord(x))
    return unique_chars[10]