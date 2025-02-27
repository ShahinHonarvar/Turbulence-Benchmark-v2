def return_nth_smallest_ascii(s):
    s = s[5:11]
    unique_chars = list(set(s))
    unique_chars.sort(key=lambda x: ord(x))
    return unique_chars[5]