def return_nth_smallest_ascii(s):
    chars = sorted((s[i] for i in range(29, 34) if s[i] != ' '))
    return chars[4] if len(chars) > 4 else None