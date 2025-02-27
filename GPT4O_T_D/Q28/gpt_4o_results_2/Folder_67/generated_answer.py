def return_nth_smallest_ascii(s):
    filtered_chars = s[60:84]
    sorted_chars = sorted(filtered_chars, key=lambda c: ord(c))
    return sorted_chars[13]