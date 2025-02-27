def return_nth_smallest_ascii(s):
    chars = [s[i] for i in range(33, 61) if s[i].isalpha()]
    chars.sort(key=ord)
    return chars[17] if len(chars) > 18 else None