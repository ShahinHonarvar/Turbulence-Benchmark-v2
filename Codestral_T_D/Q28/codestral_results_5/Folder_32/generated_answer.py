def return_nth_smallest_ascii(s):
    substring = s[14:67]
    unique_chars = list(set(substring))
    sorted_chars = sorted(unique_chars, key=lambda x: ord(x))
    return sorted_chars[7]