def return_nth_smallest_ascii(s):
    chars_in_range = [c for c in s if 32 <= ord(c) <= 67]
    chars_in_range.sort(key=lambda c: ord(c))
    if len(chars_in_range) < 12:
        return None
    else:
        return chars_in_range[11]