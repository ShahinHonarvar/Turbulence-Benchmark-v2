def return_nth_smallest_ascii(s):
    chars = [s[i] for i in range(min(7, len(s)))]
    chars.sort()
    return chars[min(6, len(chars) - 1)] if chars else None