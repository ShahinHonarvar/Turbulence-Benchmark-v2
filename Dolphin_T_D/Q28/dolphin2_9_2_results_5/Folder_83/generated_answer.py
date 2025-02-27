def return_nth_smallest_ascii(s):
    chars = [s[i] for i in range(30, 71) if s[i] not in chars]
    chars.sort(key=ord)
    return chars[14]