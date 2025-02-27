def return_nth_smallest_ascii(s):
    chars = [s[i] for i in range(min(7, len(s)))]
    chars.sort()
    return chars[6] if len(chars) > 6 else chars[-1]