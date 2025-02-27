def return_nth_smallest_ascii(s):
    chars = sorted((s[i] for i in range(44, 70) if s[i] >= ' ' and s[i] <= '~'))
    return chars[14] if len(chars) > 14 else None