def return_nth_smallest_ascii(s):
    chars = [s[i] for i in range(min(19, len(s)))]
    chars.sort()
    return chars[18] if len(chars) > 18 else None