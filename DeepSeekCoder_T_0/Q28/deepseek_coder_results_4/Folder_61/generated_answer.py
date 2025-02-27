def return_nth_smallest_ascii(s):
    chars = [s[i] for i in range(min(10, len(s)))]
    chars.sort()
    return chars[9] if len(chars) > 9 else None