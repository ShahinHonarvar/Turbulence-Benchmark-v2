def return_nth_smallest_ascii(s):
    substring = s[58:86]
    unique_chars = list(set(substring))
    unique_chars.sort(key=lambda c: ord(c))
    if len(unique_chars) > 19:
        return unique_chars[18]
    else:
        return 'Not enough characters.'