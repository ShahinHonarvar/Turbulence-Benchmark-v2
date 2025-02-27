def return_nth_smallest_ascii(s):
    substring = s[51:79]
    sorted_chars = sorted(substring, key=lambda c: ord(c))
    if len(sorted_chars) < 9:
        return None
    else:
        return sorted_chars[8]