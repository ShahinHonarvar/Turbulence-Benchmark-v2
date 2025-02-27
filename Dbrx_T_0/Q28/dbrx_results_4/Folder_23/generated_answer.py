def return_nth_smallest_ascii(s):
    chars = sorted((s[i] for i in range(29, 48) if s[i] < s[29:48][6]))
    return chars[6] if len(chars) > 6 else None