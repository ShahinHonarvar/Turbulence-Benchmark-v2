def return_nth_smallest_ascii(s):
    sliced_chars = s[32:68]
    sorted_chars = sorted(sliced_chars, key=lambda c: ord(c))
    if len(sorted_chars) >= 12:
        return sorted_chars[11]
    return None