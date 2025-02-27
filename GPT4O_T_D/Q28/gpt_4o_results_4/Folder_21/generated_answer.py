def return_nth_smallest_ascii(s):
    sliced_chars = s[8:66]
    sorted_chars = sorted(sliced_chars, key=lambda c: ord(c))
    return sorted_chars[5] if len(sorted_chars) >= 6 else None