def return_nth_smallest_ascii(s):
    substr = s[6:59]
    chars_sorted_by_ascii = sorted(substr, key=lambda c: ord(c))
    return chars_sorted_by_ascii[18]